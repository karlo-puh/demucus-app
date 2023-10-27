import os
import gradio as gr
from scipy.io.wavfile import write


def inference(audio):
  os.makedirs("out", exist_ok=True)
  write('test.wav', audio[0], audio[1])
  os.system("python3 -m demucs.separate -n htdemucs --two-stems=vocals test.wav -o out")
  return "./out/htdemucs/test/vocals.wav","./out/htdemucs/test/no_vocals.wav"
    
title = "Demucs Music Source Separation (v4)"
article = "<p style='text-align: center'><a href='https://arxiv.org/abs/1911.13254' target='_blank'>Music Source Separation in the Waveform Domain</a> | <a href='https://github.com/facebookresearch/demucs' target='_blank'>Github Repo</a> | <a href='https://www.thafx.com' target='_blank'>//THAFX</a></p>"

gr.Interface(
    inference, 
    gr.Audio(type="numpy", label="Input"),
    [gr.Audio(type="filepath", label="Vocals"),gr.Audio(type="filepath", label="No Vocals / Instrumental")],
    title=title,
    article=article,
    ).launch(enable_queue=True)