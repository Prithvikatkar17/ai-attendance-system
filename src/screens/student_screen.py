import streamlit as st
from src.ui.base_layout import  style_base_layout , style_background_dashboard
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
import numpy as np 
from PIL import Image
from src.pipelines.face_pipeline import predicted_attendance ,get_face_embeddings,model_classifier
from src.pipelines.voice_pipepine import get_voice_embedding
from src.database.db import get_all_students ,create_student
import time
from src.components.dialog_enroll import enroll_dialog


def student_dashboard():
    data = st.session_state.student_data
    c1, c2 = st.columns(2,vertical_alignment='center',gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        st.subheader(f"""
            Welcome ,{data['name']}!
            """)
        if st.button("Logout",type='secondary',icon=':material/arrow_back:',
            key='loginbackbtn',shortcut='ctrl+backspace',icon_position='left'):
            st.session_state['is_loged_in'] = False
            del st.session_state.student_data
            st.rerun()


    st.space()

    c1 ,c2 = st.columns(2)
    with c1:
        st.header("Your Enrolled Subjects ")
    with c2:
        if st.button("Enroll New Subject",type='primary',width='stretch'):
            enroll_dialog()


    footer_dashboard()

def student_screen():

    show_registration = False
       

    if "student_data" in  st.session_state :
        student_dashboard()
        return



    style_background_dashboard()
    style_base_layout()

    c1, c2 = st.columns(2,vertical_alignment='center',gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home",type='secondary',icon=':material/arrow_back:',
            key='loginbackbtn',shortcut='ctrl+backspace',icon_position='left'):
            st.session_state['login_type'] = None
            st.rerun()
    
    st.header("login using FaceID",text_alignment='center')

    st.space()
    st.space()
    
    photo_source = st.camera_input("Position your face in center")

    if photo_source is not None:
        image = np.array(Image.open(photo_source))
        detected, all_ids, num_faces = predicted_attendance(image)

        if num_faces == 0:
            st.warning("No face detected. Please try again.")
        elif num_faces > 1:
            st.warning("Multiple faces detected. Please ensure only one face is visible.")
        else:
            if detected:
                student_id = list(detected.keys())[0]
                all_students = get_all_students()
                student = next((s for s in all_students if s['student_id'] == student_id), None)

                if student:
                    st.session_state.is_logged_in = True
                    st.session_state.user_role = 'student'
                    st.session_state.student_data = student
                    st.toast(f"Welcome back {student['name']}!")
                    time.sleep(1)
                    st.rerun()
            else:
                st.info("Face not recognised! You might be a new student!")
                show_registration = True
    if show_registration:
        with st.container(border=True):
            st.header("Register new profile")
            new_name = st.text_input("Enter your name ", placeholder = "E.g. ganesh mali")


            st.subheader("Optional : voice Enrollment")
            st.info("Enroll your voice only attedance")

            audio_data = None

            try:
                audio_data = st.audio_input("Record small prases like i am present , my name is ganesh.")
            except Exception:
                st.error("audio data failed !")

            if st.button("Create Account ",type = "primary"):
                if new_name:
                    with st.spinner("Creating Profile..."):
                        img = np.array(Image.open(photo_source))
                        encoding = get_face_embeddings(img)
                        if encoding :
                            face_emb = encoding[0].tolist()  # Convert the NumPy array to a list for JSON serialization

                            voice_emb = None
                            if audio_data:
                                voice_emb = get_voice_embedding(audio_data)
                                if voice_emb is not None:
                                    voice_emb = voice_emb.tolist()  # Convert to list for JSON serialization
                            
                            response_data = create_student (new_name ,face_embedding = face_emb , voice_embedding = voice_emb)

                            if response_data:
                                model_classifier()
                                st.session_state.is_logged_in = True
                                st.session_state.user_role = 'student'
                                st.session_state.student_data = response_data[0]
                                st.toast(f'Profile created , Hi {new_name}')
                                time.sleep(1)
                                st.rerun()

                        else:
                            st.error("Couldnt Capture your facial fetures for registration")
                    

                else:
                    st.warning("Please enter your name to create a profile.")




    footer_dashboard()