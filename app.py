import os
import streamlit as st
from scipy.io.wavfile import write

def inference(audio):
    os.makedirs("out", exist_ok=True)
    write('test.wav', audio[0], audio[1])
    os.system("python3 -m demucs.separate -n htdemucs --two-stems=vocals test.wav -o out")
    return "./out/htdemucs/test/vocals.wav", "./out/htdemucs/test/no_vocals.wav"

st.title("Demucs Music Source Separation (v4)")
st.write("""
<p style='text-align: center'><a href='https://arxiv.org/abs/1911.13254' target='_blank'>Music Source Separation in the Waveform Domain</a> |
<a href='https://github.com/facebookresearch/demucs' target='_blank'>Github Repo</a> |
<a href='https://www.thafx.com' target='_blank'>//THAFX</a></p>
""", unsafe_allow_html=True)

uploaded_audio = st.file_uploader("Upload an audio file", type=["wav"])

if uploaded_audio is not None:
    audio_data = uploaded_audio.read()
    st.audio(audio_data, format="audio/wav", start_time=0)
    
    if st.button("Separate Vocals"):
        separated_vocals, separated_instrumental = inference((audio_data, 44100))  # Adjust the sample rate accordingly
        st.audio(separated_vocals, format="audio/wav", start_time=0, key="vocals")
        st.audio(separated_instrumental, format="audio/wav", start_time=0, key="instrumental")
