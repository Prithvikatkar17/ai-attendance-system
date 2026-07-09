import streamlit as st 
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
import time


@st.dialog("Create New Subject")
def enroll_dialog():
    st.write("Enter Subject code Provided by your Teacher to Enroll")
    join_code = st.text_input("Subject Code",placeholder="CS101")

    if st.button('Enroll now' ,type='primary',width='stretch',):
        if join_code:
            res = supabase.table("subjects").select("*").eq("subject_code",join_code).execute()
            if res.data :
                subject = res.data[0]
                student_id = st.session_state.student_data['student_id']

                check = supabase.table('subject_students').select("*").eq("student_id",student_id).eq("subject_id",subject['subject_id']).execute()
                if check.data:
                    st.warning("You are already enrolled in this Program")
                else:
                    enroll_student_to_subject(student_id, subject['subject_id'])
                    st.success(f"Successfully Enrolled to {subject['name']}")
                    time.sleep(1)
                    st.rerun()
        else:
            st.warning("Please Enter Subject Code")