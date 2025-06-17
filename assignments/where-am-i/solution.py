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