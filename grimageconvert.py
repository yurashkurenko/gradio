import gradio as gr
from PIL import Image
import subprocess

def convert_image(image):
    image.save("input.png")  # сохраняем изображение как input.png
    subprocess.run(["convert", "input.png", "output.jpg"])  # конвертируем изображение с помощью ImageMagick
    return "output.jpg"

demo = gr.Interface(
    fn=convert_image,
    inputs=gr.Image(label="Изображение для конвертирования"),
    outputs=gr.Image(label="Конвертированное изображение"),
    title="Конвертирование изображения из png в jpg",
    description="Загрузите изображение в формате png и нажмите кнопку 'Submit', чтобы конвертировать его в jpg."
)

demo.launch()
