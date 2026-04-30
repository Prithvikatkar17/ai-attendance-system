import numpy as np 
import dlib
import face_rcognition_models 
from sklearn.svm import SVC
import streamlit as st 

from src.database.db import get_all_students



@st.cache_resource   # Cache the loaded models to avoid reloading on every run
def load_dlib_models():
    # Load the dlib models for face detection and recognition
    detector = dlib.get_frontal_face_detector()


    sp = dlib.shape_predictor(
        face_rcognition_models.pose_predictor_model_location()
        )
    
    facerec = dlib.face_recognition_model_v1(
        face_rcognition_models.face_recognition_model_location()
        )
    
    return detector, sp, facerec

def get_face_embeddings(image_np):
    detector, sp, facerec = load_dlib_models()
    face = detector(image_np, 1) # 1 means upsample the image once to detect smaller faces


    encoding = []
    for face in face:
        shape = sp(image_np, face)
        face_descriptor = facerec.compute_face_descriptor(image_np, shape ,1)  #128 embeddings
        encoding.append(np.array(face_descriptor))

    return encoding