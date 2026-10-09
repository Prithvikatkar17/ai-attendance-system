import streamlit as st

def header_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <style>
        .attendly-logo-title {{
            font-size: 4.2rem !important;
            font-weight: 800 !important;
            letter-spacing: -2px !important;
            color: #FFFFFF !important;
            text-shadow: 0 4px 20px rgba(255, 255, 255, 0.4) !important;
            margin-top: 10px !important;
            margin-bottom: 0px !important;
            text-align: center !important;
            line-height: 1.1 !important;
        }}
        .attendly-logo-subtitle {{
            text-align: center !important;
            font-size: 1.1rem !important;
            font-weight: 500 !important;
            color: rgba(255, 255, 255, 0.85) !important;
            letter-spacing: 0.5px !important;
            margin-top: 0px !important;
        }}
        </style>
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:40px; margin-top:20px">
            <img src='{logo_url}' style='height:90px; filter: drop-shadow(0 6px 12px rgba(0,0,0,0.15));' />
            <h1 class="attendly-logo-title">Attendly</h1>
            <p class="attendly-logo-subtitle">Next-Gen AI Attendance</p>
        </div>   
                
                """, unsafe_allow_html=True)




def header_dashboard():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='{logo_url}' style='height:85px;' />
            <h2 style='text-align:left;'>ATTENDLY</h2>
        </div>   
                
                """, unsafe_allow_html=True)