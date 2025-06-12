import os
from PIL import Image

def show_image(image_path):
    if os.path.exists(image_path):
        image = Image.open(image_path)
        image.show()