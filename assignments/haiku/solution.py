from ai import call_gpt

def main():
    # Get the user's input
    name = input("Enter your name: ")
    topic = input("Enter a topic: ")
    print("Creating your haiku...")
    print()

    # Use GPT to generate a haiku
    haiku = call_gpt(f"Generate me a haiku about {topic} and {name}!")
    print(haiku)

if __name__ == "__main__":
    main()