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

@st.cache_resource
def get_model_trained():
    X = []
    y = []

    student_db = get_all_students()

    if not student_db:
        return None
    for student in student_db:
        embeding = student.get('face_embedding')
        if embeding:
            X.append(np.array(embeding))
            y.append(student.get('student_id'))

    if len(X) == 0:
        return None
    

    clf = SVC(kernel='linear', probability=True,class_weight='balanced') # Using a linear kernel for SVM and enabling probability estimates. class_weight='balanced' helps to handle imbalanced datasets by assigning weights inversely proportional to class frequencies.

    try: 
        clf.fit(X,y)
    except ValueError:
        pass
# This function retrieves all student records from the database, extracts their face embeddings, and trains an SVM model to classify the embeddings based on student IDs. The trained model is cached to avoid retraining on every run, improving performance. If there are no students or embeddings available, it returns None.


def model_classifier():
    st.cache_resource.clear()  # Clear the cache to force retraining of the model with updated data
    model_data = get_model_trained()
    return bool(model_data) 
# This function clears the cache to ensure that the model is retrained with the most recent data from the database. It then calls get_model_trained() to train the model and returns True if the model was successfully trained (i.e., if there is training data available), or False if there was no data to train on.