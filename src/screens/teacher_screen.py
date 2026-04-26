import streamlit as st
from src.ui.base_layout import  style_base_layout , style_background_dashboard
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard

def teacher_screen():
    style_background_dashboard()
    style_base_layout()
    teacher_screen_login()

    
def teacher_screen_login():
    c1, c2 = st.columns(2,vertical_alignment='center',gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        st.button("Go back to Home",type='secondary',icon=':material/arrow_back:',
                  key='loginbackbtn',shortcut='ctrl+backspace',
                  icon_position='left',on_click=lambda: st.session_state.update({'login_type':None}))
    
    st.space()
    st.space()

    st.subheader('login using passworsd',text_alignment='center')

    st.space()
    st.space()

    teacher_input = st.text_input("Enter Username",placeholder="Username",type='default')
    password_input = st.text_input("Enter Password",placeholder="Password",type='password')


    btn1 ,btn2 = st.columns(2)
    with btn1:
        st.button("login",icon=':material/passkey:',shortcut='control + enter',width='stretch')
    with btn2:
        st.button("register instead",icon=':material/passkey:',type='primary',width='stretch')

    st.divider()
    
    footer_dashboard()



def teacher_screen_register():  
    c1, c2 = st.columns(2,vertical_alignment='center',gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        st.button("Go back to Home",type='secondary',icon=':material/arrow_back:',
                  key='loginbackbtn',shortcut='ctrl+backspace',
                  icon_position='left',on_click=lambda: st.session_state.update({'login_type':None}))
        
    st.space()
    st.space()

    st.subheader('login using passworsd',text_alignment='center')

    st.space()
    st.space()

    teacher_input = st.text_input("Enter Username",placeholder="Username",type='default')
    password_input = st.text_input("Enter Password",placeholder="Password",type='password')


    btn1 ,btn2 = st.columns(2)
    with btn1:
        st.button("login",icon=':material/passkey:',shortcut='control + enter',width='stretch')
    with btn2:
        st.button("register instead",icon=':material/passkey:',type='primary',width='stretch')


    st.divider()
    
    footer_dashboard()


        
    st.header("Teacher Screen")