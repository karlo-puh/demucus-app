import os
import streamlit as st
from scipy.io.wavfile import write
import subprocess

st.title("Demucs Music Source Separation (v4)")
st.markdown("Music Source Separation in the Waveform Domain | [Github Repo](https://github.com/facebookresearch/demucs) | [//THAFX](https://www.thafx.com)")

audio_input = st.file_uploader("Upload an audio file", type=["wav"])

if st.button("Process"):
    os.makedirs("out", exist_ok=True)
    with open('test.wav', 'wb') as audio_file:
        audio_file.write(audio_input.read())

    cmd = "python3 -m demucs.separate -n htdemucs --two-stems=vocals test.wav -o out"
    subprocess.run(cmd, shell=True)

    vocals_path = "./out/htdemucs/test/vocals.wav"
    no_vocals_path = "./out/htdemucs/test/no_vocals.wav"
