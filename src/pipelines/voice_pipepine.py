

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
    