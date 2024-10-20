import numpy as np
import gradio as gr

def imwork(input_img):
    return input_img

demo = gr.Interface(imwork, gr.Image(), "image")
if __name__ == "__main__":
    demo.launch()
