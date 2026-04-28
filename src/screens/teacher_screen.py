import streamlit as st
from src.ui.base_layout import  style_base_layout , style_background_dashboard
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard

def teacher_screen():
    style_background_dashboard()
    style_base_layout()
    


    if 'teacher_login_type' not in  st.session_state or st.session_state.teacher_login_type=="login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()
    
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
            st.session_state.teacher_login_type = 'login'
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
        st.button("Resister now",icon=':material/passkey:',shortcut='control + enter',width='stretch')
            
    with btnc2:
        if st.button("login instead",icon=':material/passkey:',type='primary',width='stretch'):
            st.session_state.teacher_login_type = 'login'


    st.divider()
    
    footer_dashboard()


        
    