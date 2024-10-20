import gradio as gr
from wand.image import Image

def convert_png_to_jpg(input_image):
    with Image(blob=input_image) as img:
        img.format = 'jpg'
        jpg_blob = img.make_blob('jpg')
    return jpg_blob

iface = gr.Interface(
    fn=convert_png_to_jpg,
    inputs=gr.inputs.Image(type="file"),
    outputs=gr.outputs.Image(type="file"),
    title="PNG to JPG Converter",
    description="Convert PNG images to JPG format using ImageMagick."
)

if __name__ == "__main__":
    iface.launch()
