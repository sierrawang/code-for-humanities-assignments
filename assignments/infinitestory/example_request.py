from openai import OpenAI
import json

# If you want to use your own GPT
# client = OpenAI(api_key="your_openai_api_key")
CLIENT = OpenAI(api_key="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")


def main():
    print("[Suspenseful music plays in the background]")

    # I kept the API exacty the same as OpenAI's API
    chat_completion = CLIENT.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "What is the capital of all countries in east africa? Reply in json where keys are countries",
            }
        ],
        model="gpt-3.5-turbo", # the GPT model to use
        response_format={"type": "json_object"} # we want our response in json format,
    )
    response_str = chat_completion.choices[0].message.content
    response = json.loads(response_str)
    print(response)


if __name__ == "__main__":
    main()
