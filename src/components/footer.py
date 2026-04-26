import streamlit as st

def footer_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div style="margin-top:50px; display:flex; flex-direction:column; align-items:center; justify-content:center;">
                <p> Created with ❤️ by SnapRoll Team </p>
        </div>   
                
                """, unsafe_allow_html=True)
