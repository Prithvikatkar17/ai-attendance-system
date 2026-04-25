import streamlit as st

def home_screen():
    st.header("Home Screen")


    col1, col2 = st.columns(2)

    with col1:
        if st.button("Teacher Login"):
            st.session_state['login_type'] = 'teacher'
            st.rerun()
    
    with col2:
        if st.button("Student Login"):
            st.session_state['login_type'] = 'student'
            st.rerun()