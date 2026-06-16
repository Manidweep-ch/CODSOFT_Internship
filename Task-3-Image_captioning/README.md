# Image Captioning using BLIP

## Introduction

This project is an AI-based Image Captioning System developed as part of the CodSoft Artificial Intelligence Internship.

The system takes an image as input and generates a meaningful text description (caption) using a pre-trained BLIP (Bootstrapping Language-Image Pre-training) model from Hugging Face.

---

## Features

* Upload an image
* Generate captions automatically
* Uses a pre-trained BLIP model
* Simple and user-friendly interface
* Supports different types of images

---

## Technologies Used

* Python
* Transformers (Hugging Face)
* PyTorch
* Pillow (PIL)
* Gradio

---

## How It Works

1. User uploads an image.
2. The image is processed using the BLIP Processor.
3. The BLIP Model analyzes the image.
4. A caption is generated.
5. The generated caption is displayed to the user.

### Workflow

Image → BLIP Processor → BLIP Model → Generated Caption

---

## Installation

Install the required libraries:

```bash
pip install transformers
pip install torch
pip install pillow
pip install gradio
```

---

## Running the Project

Run the following command:

```bash
python image_caption.py
```

After execution, Gradio will generate a local web interface where users can upload images and generate captions.

---

## Sample Output

### Input Image

Dog playing on grass

### Generated Caption

A dog running across a green lawn.

---

## Applications

* Image Understanding
* Accessibility Tools for Visually Impaired Users
* Content Generation
* Photo Organization
* AI-based Image Analysis

---

## Conclusion

This project demonstrates how Computer Vision and Natural Language Processing can be combined to automatically generate captions for images using a pre-trained AI model.
