from openai import OpenAI
import base64

# Define my **SECRET** API key
OPENAI_API_KEY = ""

# Initialize an OpenAI client to be able to connect to the OpenAI API
client = OpenAI(api_key = OPENAI_API_KEY)

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def main():
    # Path to your image
    image_path = "horses.jpeg"

    # Getting the Base64 string
    base64_image = encode_image(image_path)

    # Send the messages to GPT
    response = client.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "user",
                "content": [
                    { "type": "input_text", "text": "What is the breed of this horse? Respond only with the breed." },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{base64_image}",
                    },
                ],
            }
        ],
    )

    print(response.output_text)

if __name__ == '__main__':
    main()