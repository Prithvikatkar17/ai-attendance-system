import streamlit as st



def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: linear-gradient(135deg, #1A2980 0%, #26D0CE 100%) !important;
                    background-attachment: fixed !important;
                    color: #FFFFFF !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color: rgba(255, 255, 255, 0.1) !important;
                    backdrop-filter: blur(16px) !important;
                    -webkit-backdrop-filter: blur(16px) !important;
                    padding:2.5rem !important;
                    border-radius: 24px !important;
                    border: 1px solid rgba(255, 255, 255, 0.2) !important;
                    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.2) !important;
                    }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: linear-gradient(135deg, #1A2980 0%, #26D0CE 100%) !important;
                    background-attachment: fixed !important;
                    color: #FFFFFF !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
# asdasd
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: 'Outfit', sans-serif !important;
                font-size: 3.5rem !important;
                font-weight: 800 !important;
                line-height:1.1 !important;
                margin-bottom:0rem !important;
                color: #FFFFFF !important;
                letter-spacing: -0.05em !important;
            }
                

            h2 {
                font-family: 'Outfit', sans-serif !important;
                font-size: 2rem !important;
                font-weight: 700 !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
                color: #FFFFFF !important;
                letter-spacing: -0.03em !important;
            }
                
            h3, h4, p {
                font-family: 'Outfit', sans-serif;    
                color: rgba(255, 255, 255, 0.9) !important;
            }
                

            button{
                border-radius: 12px !important;
                background-color: #FFFFFF !important;
                color: #1A2980 !important;
                font-weight: 700 !important;
                font-family: 'Outfit', sans-serif !important;
                padding: 10px 24px !important;
                border: none !important;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1) !important;
                transition: all 0.2s ease-in-out !important;
                }
            
            button p {
                color: #1A2980 !important;
            }

            button[kind="secondary"]{
                border-radius: 12px !important;
                background-color: rgba(255, 255, 255, 0.2) !important;
                color: #FFFFFF !important;
                font-weight: 700 !important;
                font-family: 'Outfit', sans-serif !important;
                padding: 10px 24px !important;
                border: 1px solid rgba(255, 255, 255, 0.4) !important;
                box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
                transition: all 0.2s ease-in-out !important;
                }
                
            button[kind="secondary"] p {
                color: #FFFFFF !important;
            }

            button[kind="tertiary"]{
                border-radius: 12px !important;
                background-color: rgba(0, 0, 0, 0.2) !important;
                color: #FFFFFF !important;
                font-weight: 500 !important;
                font-family: 'Outfit', sans-serif !important;
                padding: 10px 24px !important;
                border: 1px solid rgba(255, 255, 255, 0.1) !important;
                transition: all 0.2s ease-in-out !important;
                }
                
            button[kind="tertiary"] p {
                color: #FFFFFF !important;
            }

            button:hover{
                transform: translateY(-2px);
                box-shadow: 0 8px 20px rgba(0,0,0,0.2) !important;
                }
        </style>  

                """
            ,unsafe_allow_html=True)