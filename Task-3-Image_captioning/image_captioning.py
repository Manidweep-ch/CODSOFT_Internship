from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import gradio as gr

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image):

    inputs = processor(image,return_tensors="pt")

    output = model.generate(**inputs,max_new_tokens=50)

    caption = processor.decode(output[0],skip_special_tokens=True)

    return caption


app = gr.Interface(
    fn=generate_caption,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="Image Caption Generator"
)

app.launch()