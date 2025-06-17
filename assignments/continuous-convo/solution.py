from openai import OpenAI

client = OpenAI(api_key="your api key here")  # Replace with your actual OpenAI API key

def get_next_message(conversation):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation
        )

        return response.choices[0].message.content.strip()

def main():
    conversation = []
    # Accept the first message from the user and add it to the conversation list
    user_input = input("You: ")
    conversation.append({"role": "user", "content": user_input})

    # While the user input is not empty, keep the conversation going
    while user_input != "":
        # Get the next message from the AI based on the conversation history
        next_message = get_next_message(conversation)
        # Print the AI's response and append it to the conversation
        print(f"AI: {next_message}")

        # Append the AI's response to the conversation
        conversation.append({"role": "assistant", "content": next_message})

        # Get the next user input and append it to the conversation
        user_input = input("You: ")
        conversation.append({"role": "user", "content": user_input})


if __name__ == "__main__":
    main()