from openai import OpenAI

client = OpenAI(api_key="your api key here")  # Replace with your actual OpenAI API key

def get_next_message(conversation):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation
        )

        return response.choices[0].message.content.strip()

def main():
    conversation = [{
         "role": "developer",
         "content":  "You are co-writing a story with a user. They will provide a sentence, then you will continue the story with a sentence of your own, then they will provide another and so on. Don't say more than one sentence "
    }]
    user_input = input("Start the story: ")
    conversation.append({"role": "user", "content": user_input})

    while user_input != "":
        next_message = get_next_message(conversation)
        print(f"The story continues: {next_message}")

        conversation.append({"role": "assistant", "content": next_message})

        user_input = input("Continue the story: ")
        conversation.append({"role": "user", "content": user_input})


if __name__ == "__main__":
    main()