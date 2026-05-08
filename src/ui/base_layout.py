import streamlit as st



def style_background_dashboard():
    st.markdown("""

    <style>
            .stApp {
                background-color: #0D1B2A   !important;
            }
        
    </style>
        """
                , unsafe_allow_html=True)
    


    
def style_background_home():
    st.markdown("""

    <style>
           .stApp {
                background-color: #0F172A   !important;
            }
            .stApp div[data-testid="stColumn"] { 
                background-color: #2563EB  !important;
                border-radius: 5rem !important;
                padding: 2rem !important;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1) !important;
        
    </style>
        """
                , unsafe_allow_html=True)
    




def style_base_layout():
    st.markdown("""

    <style>
                
        @import url('https://fonts.googleapis.com/css2?family=Big+Shoulders:opsz,wght@10..72,100..900&family=Climate+Crisis:YEAR@1979&family=Russo+One&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap');


        # /* hide top bar of streamlit */
        # #MainMenu ,footer, header {
        #     visibility: hidden;   
        #         }
        # .block-container {
        #         padding-top: 1.5rem  !important;
        #         }  
        
                
        h1{
            font-family: 'Climate Crisis', sans-serif !important; 
            font-size: 3.5rem !important;
            line-height: 1.1 !important; 
            margin-bottom: 0rem !important;   
            }
                
         h2{
            font-family: 'Climate Crisis', sans-serif !important; 
            font-size: 2rem !important;
            line-height: 1.1 !important; 
            margin-bottom: 0rem !important;   
            color: #E0E3FF !important;
            }

        h3{
            font-family: 'Russo One', sans-serif !important;
            font-size: 1.5rem !important;}    


        h4,p{
            font-family: 'Bebas Neue', sans-serif !important;
        }
                
        button[kind="primary"] {
                border-radius: 1.5rem !important;
                background-color: #10B981 !important;
                color: white !important;
                padding: 0.5rem 1.5rem !important;
                border: none !important;
                transition: transform 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
                }


        button[kind="secondary"] {
                border-radius: 1.5rem !important;
                background-color: #F59E0B !important;
                color: white !important;
                padding: 0.5rem 1.5rem !important;
                border: none !important;
                transition: transform 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
                }


        button[kind="tertiary"] {
                border-radius: 1.5rem !important;
                background-color: #8B5CF6   !important;
                color: white !important;
                padding: 0.5rem 1.5rem !important;
                border: none !important;
                transition: transform 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
                }

        button:hover {
                transform: scale(1.05) !important;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2) !important;
                }

    </style>
        """
                , unsafe_allow_html=True)