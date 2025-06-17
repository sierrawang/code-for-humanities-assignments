from openai import OpenAI

client = OpenAI(api_key="your api key here")  # Replace with your actual OpenAI API key

def main():
    # Define the prompt for the pirate translator
    type_of_translation = input("Enter the type of translation (e.g., 'pirate', 'Shakespeare'): ")
    prompt = input(f"Enter the English text to translate to {type_of_translation} speak: ")

    # Call the OpenAI API to get the translation
    response = client.responses.create(
        model="gpt-4o-mini",
        input=f"Translate the following text to {type_of_translation} speak:\n\n{prompt}",
    )

    # Extract and print the translated text
    translation = response.output_text
    print(f"{type_of_translation} Translation: {translation}")

if __name__ == '__main__':
    main()