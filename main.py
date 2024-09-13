from rembg import remove
from PIL import Image
import os
import numpy as np
import io

input_folder = r'C:\caminho\para\a\pasta\de\entrada'
output_folder = r'C:\caminho\para\a\pasta\de\saida\semFundo'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Open the image file
        with open(input_path, "rb") as f:
            input_image = f.read()

        # Use rembg to remove the background
        output_image = remove(input_image)

        # Convert the output bytes back to a PIL Image
        output_image = Image.open(io.BytesIO(output_image))

        # Convert RGBA image to RGB if needed (JPEG does not support alpha channel)
        if output_image.mode == "RGBA":
            output_image = output_image.convert("RGB")

        # Save the processed image
        output_image.save(output_path)

print("Background removal completed for all images.")
