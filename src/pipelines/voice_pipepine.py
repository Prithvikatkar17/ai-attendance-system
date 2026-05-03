

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



def process_bulk_audio(audio_bytes , candidates_dict , threshold=0.65):
    try:
        encoder = load_voice_encoder()
        audio , sr = librosa.load(io.BytesIO(audio_bytes), sr=16000)
        segments = librosa.effects.split(audio, top_db=30)

        identifiied_results = {}

        for start ,end in segments:
            if (end -start)<sr*0.5:
                continue
            segment_audio = audio[start:end]
            wav = preprocess_wav(segment_audio)
            embedding = encoder.embed_utterance(wav)

            sid , score = identify_speaker(embedding , candidates_dict , threshold)
            if sid:
                if sid not in identifiied_results or score > identifiied_results[sid]:
                    identifiied_results[sid] = score

        return identifiied_results
    except Exception as e:
        st.error("bulk audio processing error")
        return {} 