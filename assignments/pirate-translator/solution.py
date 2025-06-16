from openai import OpenAI

client = OpenAI(api_key="your api key here")

def main():
    # Define the prompt for the pirate translator
    type_of_translation = input("Enter the type of translation (e.g., 'pirate', 'Shakespeare'): ")
    prompt = input(f"Enter the English text to translate to {type_of_translation} speak: ")

    # Call the OpenAI API to get the translation
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "system",
            "content": f"You are a {type_of_translation} translator. Translate English text to {type_of_translation} speak."
        }, {
            "role": "user",
            "content": prompt
        }],
        max_tokens=50
    )

    # Extract and print the translated text
    translation = response.choices[0].message.content.strip()
    print(f"{type_of_translation} Translation: {translation}")

if __name__ == '__main__':
    main()