from openai import OpenAI
import base64

FILENAMES = [
    "almanac.png",
    "book.jpeg",
    "notebook.jpeg",
]

client = OpenAI(api_key="your api key here")  # Replace with your actual OpenAI API key

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
    


def main():
    for filename in FILENAMES:
        image_path = f"data/{filename}"

        base64_image = encode_image(image_path)

        # Create the request
        response = client.responses.create(
            model="gpt-4o",
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": "Transcribe the text in this image. If you are unsure, provide your best guess based on the image.",
                        },
                        {
                            "type": "input_image",
                            "image_url":  f"data:image/jpeg;base64,{base64_image}"
                        }
                    ]
                }
            ],
        )

        with open(f"transcribed_{filename.split()[0]}.txt", "w") as f:
            f.write(response.output_text.strip())

if __name__ == '__main__':
    main()