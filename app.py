import os
import streamlit as st

def inference(audio_data):
    os.makedirs("out", exist_ok=True)
    
    # Save the uploaded audio data as a WAV file
    with open('test.wav', 'wb') as audio_file:
        audio_file.write(audio_data)
    
    # Perform separation here (replace this line with your separation code)
    os.system("python3 -m demucs.separate -n htdemucs --two-stems=vocals test.wav -o out")
    
    return "./out/htdemucs/test/vocals.wav", "./out/htdemucs/test/no_vocals.wav"

st.title("Demucs Music Source Separation (v4)")

uploaded_audio = st.file_uploader("Upload an audio file", type=["wav"])

if uploaded_audio is not None:
    audio_data = uploaded_audio.read()
    st.audio(audio_data, format="audio/wav", start_time=0)
    
    if st.button("Separate Vocals"):
        separated_vocals, separated_instrumental = inference(audio_data)
        st.audio(separated_vocals, format="audio/wav", start_time=0)
        st.audio(separated_instrumental, format="audio/wav", start_time=0)
