# Where am I?
In this challenge, you will pass in a picture of a location to the OpenAI API, with a prompt asking the AI to identify the location in the image. The AI will then return a description of the location, which you can use to determine where you are.

We have given you 5 sample images to test your program with, which you can find in the `images` folder. You can also use your own images to test the program.

hawaii.jpeg - Taken in Oahu, Hawaii
ri.jpeg - Taken in Cranston, Rhode Island
sf.jpeg - Taken in Chinatown, San Francisco, California
stanford.jpeg - Taken in Escondido Village Graduate Residences, Stanford University, California
north-carolina.jpeg - Taken in North Carolina

The images are meant to range from vague to detailed, so you can see how well the AI can identify the location based on the image alone.

# Extension
Try all images with both of the following models:
- gpt-4o
- gpt-4.1

There is a noticeable difference in the quality of response.


```python
from openai import OpenAI
import base64

client = OpenAI(api_key="your api key here")


# Load your image and encode it in base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
    

def main():
    image_path = "data/north-carolina.jpeg"

    base64_image = encode_image(image_path)

    # Create the request
    response = client.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": "Where was this photograph taken? Please provide a detailed description of the location. Even if you are unsure, provide your best guess based on the image.",
                    },
                    {
                        "type": "input_image",
                        "image_url":  f"data:image/jpeg;base64,{base64_image}"
                    }
                ]
            }
        ],
    )

    print(response.output_text.strip())


if __name__ == '__main__':
    main()
```