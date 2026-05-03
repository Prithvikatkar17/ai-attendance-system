

from resenmblyzer import VoiceEncoder, preprocess_wav
import numpy as np
import streamlit as st
import io
import librosa 


@st.cache_resource
def load_voice_encoder():
    
    return VoiceEncoder()


def get_voice_embedding(audio_bytes):
    try:
        encoder = load_voice_encoder()

        audio, sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)
        wav = preprocess_wav(audio)
        embeding = encoder.embed_utterance(wav)
        return embeding.tolist()
    except Exception as e:
        st.error("voice recog error")
        return None
    


def identify_speaker(new_embedding,candidates_dict , threshold=0.65):
    if new_embedding is None or not candidates_dict:
        return  None ,0.0
    
    best_sid = None
    best_score = -1.0

    for sid , stored_embedding in candidates_dict.items():
        if stored_embedding:
            similarity = np.dot(new_embedding,stored_embedding)
            if similarity > best_score:
                best_score = similarity
                best_sid = sid
    
    if best_score >= threshold:
        return best_sid , best_score
    
    return None , best_score 

