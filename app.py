import os
import streamlit as st
from scipy.io.wavfile import write
import subprocess

st.title("Demucs Music Source Separation (v4)")
st.markdown("Music Source Separation in the Waveform Domain | [Github Repo](https://github.com/facebookresearch/demucs) | [//THAFX](https://www.thafx.com)")

audio_input = st.file_uploader("Upload an audio file", type=["wav"])

if audio_input is not None:
    os.makedirs("out", exist_ok=True)
    with open('test.wav', 'wb') as audio_file:
        audio_file.write(audio_input.read())

    cmd = "python3 -m demucs.separate -n htdemucs --two-stems=vocals test.wav -o out"
    subprocess.run(cmd, shell=True)

    vocals_path = "./out/htdemucs/test/vocals.wav"
    no_vocals_path = "./out/htdemucs/test/no_vocals.wav"

    st.audio(vocals_path, format="audio/wav", label="Vocals")
    st.audio(no_vocals_path, format="audio/wav", label="No Vocals / Instrumental")
