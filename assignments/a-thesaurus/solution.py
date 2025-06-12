import json

filename = "a.json"

def main():
    # TODO: Your code goes here!
    with open(filename, 'r') as file:
        data = json.load(file)

    word = input("Enter a word to find synonyms: ")
    while word != "":
        word = word.upper()
        if word in data:
            print(f"Synonyms for '{word}': {', '.join(data[word])}")
        else:
            print(f"No synonyms found for '{word}'")
        word = input("Enter another word to find synonyms (or press Enter to exit): ")

if __name__ == '__main__':
    main()


