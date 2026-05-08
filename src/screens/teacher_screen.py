
import streamlit as st
from src.ui.base_layout import  style_base_layout , style_background_dashboard
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.database.db import check_teacher_exists, create_teacher, teacher_login



def teacher_screen():
    style_background_dashboard()
    style_base_layout()
    
    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif 'teacher_login_type' not in  st.session_state or st.session_state.teacher_login_type=="login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()



def teacher_dashboard():
    data = st.session_state.teacher_data
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
            del st.session_state.teacher_data
            st.rerun()

    
    st.space()

    if 'current_teacher_tab' not in st.session_state:
        st.session_state.current_teacher_tab = 'take_attendance'

    tab1 ,tab2,tab3 = st.columns(3)

    with tab1:
        type1="primary" if  st.session_state.current_teacher_tab == 'take_attendance' else "tertiary"
        if st.button('Take attendance', type = type1 , width='stretch',icon =':material/ar_on_you:'):
            st.session_state.current_teacher_tab = 'take_attendance'
            st.rerun()

    with tab2:
        type2 = "primary" if  st.session_state.current_teacher_tab == 'manage_subjects' else "tertiary"
        if st.button('Manage Subjects',type = type2 ,width='stretch',icon =':material/book_ribbon:'):
            st.session_state.current_teacher_tab = 'manage_subjects'
            st.rerun()

    with tab3:
        type3 = "primary" if  st.session_state.current_teacher_tab == 'attendance_records' else "tertiary"

        if st.button('Attendance Records',type = type3 ,width='stretch',icon =':material/cards_stack:'):
            st.session_state.current_teacher_tab = 'attendance_records'
            st.rerun()

    footer_dashboard()

    




def login_teacher(username,password):
    if not username or not password:
        return False
    teacher = teacher_login(username,password)

    if teacher:
        st.session_state.user_role = 'teacher'
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True
        return True


def register_teacher(teacher_username,teacher_pass,teacher_pass_confirm,teacher_name):
    if not teacher_username or not teacher_pass or not teacher_pass_confirm or not teacher_name:
        return False , "All fields are required!"
    if check_teacher_exists(teacher_username):
        return False , "Username already exists!"
    if teacher_pass != teacher_pass_confirm:
        return False , "Passwords do not match!"
    
    try:
        create_teacher(teacher_username, teacher_pass,teacher_name)
        return True , "registered successfully! You can now login."
    except Exception as e:
        return False , "An error occurred during registration. Please try again."
# this function validates the input fields for teacher registration, checks if the username already exists, 
# and if the passwords match. If all validations pass, it creates a new teacher record in the database. 
# It returns a success status and a message indicating the result of the registration attempt.






def teacher_screen_login():
    c1, c2 = st.columns(2,vertical_alignment='center',gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home",type='secondary',icon=':material/arrow_back:',
                  key='loginbackbtn',shortcut='ctrl+backspace',icon_position='left'):
            st.session_state['login_type'] = None
            st.rerun()
    
    st.space()
    st.space()

    st.subheader('login using passworsd',text_alignment='center')

    st.space()
    st.space()

    teacher_input = st.text_input("Enter Username",placeholder="Username",type='default')
    password_input = st.text_input("Enter Password",placeholder="Password",type='password')


    btnc1 ,btnc2 = st.columns(2)
    with btnc1:
        if st.button("login",icon=':material/passkey:',shortcut='control + enter',width='stretch'):
            if login_teacher(teacher_input,password_input):
                st.toast("Welcome back!",icon="👋")  # The st.toast() function is used to display a temporary notification message to the user.
                import time
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid username or password.")
    with btnc2:
        if st.button("register instead",icon=':material/passkey:',type='primary',width='stretch'):
            st.session_state.teacher_login_type = 'register'

    st.divider()
    
    footer_dashboard()








def teacher_screen_register():  
    c1, c2 = st.columns(2,vertical_alignment='center',gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home",type='secondary',icon=':material/arrow_back:',
                  key='loginbackbtn',shortcut='ctrl+backspace',icon_position='left'):
            st.session_state['login_type'] = None
            st.rerun()
    

    st.space()
    st.space()

    st.subheader('Register your Teacher profile',text_alignment='center')

    st.space()
    st.space()

    teacher_username = st.text_input("Enter Username",placeholder="Username",type='default')
    teacher_name = st.text_input("Enter name",placeholder="name",type='default')



    teacher_pass = st.text_input("Enter Password",placeholder="Password",type='password')
    teacher_pass_confirm = st.text_input("Confirm Password",placeholder="Confirm Password",type='password')


    btnc1 ,btnc2 = st.columns(2)
    with btnc1:
        if st.button("Resister now",icon=':material/passkey:',shortcut='control + enter',width='stretch'):
            success ,message = register_teacher(teacher_username,teacher_pass,teacher_pass_confirm,teacher_name)
            if success:
                st.success(message)
                import time
                time.sleep(2)
                st.session_state.teacher_login_type = 'login'
                st.rerun()
            else:
                st.error(message)
            
    with btnc2:
        if st.button("login instead",icon=':material/passkey:',type='primary',width='stretch'):
            st.session_state.teacher_login_type = 'login'


    st.divider()
    
    footer_dashboard()


        
    