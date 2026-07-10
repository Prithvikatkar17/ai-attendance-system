import streamlit as st 
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
import time


@st.dialog("Create New Subject")
def enroll_dialog():