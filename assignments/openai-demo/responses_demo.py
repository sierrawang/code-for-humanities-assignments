from openai import OpenAI

# Define my **SECRET** API key
OPENAI_API_KEY = ""

# Initialize an OpenAI client to be able to connect to the OpenAI API
client = OpenAI(api_key = OPENAI_API_KEY)

def main():
    # Call GPT
    response = client.responses.create(
        model="gpt-4o-mini",
        input="Write a one-sentence bedtime story about a unicorn."
    )

    # Print GPT's response
    print(response.output_text)

if __name__ == '__main__':
    main()