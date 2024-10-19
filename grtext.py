#display a text
import gradio as gr

def text_display(text):
    return text

demo = gr.Interface(text_display, gr.Text(), "text")
#alternatively use gr.TextBox()
demo.launch()
