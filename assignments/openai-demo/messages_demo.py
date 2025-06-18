from openai import OpenAI

# Define my **SECRET** API key
OPENAI_API_KEY = ""

# Initialize an OpenAI client to be able to connect to the OpenAI API
client = OpenAI(api_key = OPENAI_API_KEY)

def main():
    # Send the messages to GPT
    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "developer",
                "content": "Talk like a pirate and respond in one sentence."
            },
            {
                "role": "user",
                "content": "What is an API?"
            }
        ]
    )
    print(response)

    print(response.output_text)

if __name__ == '__main__':
    main()