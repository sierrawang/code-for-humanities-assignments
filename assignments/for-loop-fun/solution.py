

def main():
    my_list = ["I", "love", "to", "code", "!"]

    # Convert my list to a string with a space between each word
    phrase = ""
    for word in my_list:
        phrase += f"{word} "
    
    # Print out the resulting phrase
    print(f"Original phrase: {phrase}")

    # Change the excalamation point to be the word "so"
    my_list[4] = "so"

    # Append the word "much"
    my_list.append("much")

    # Convert my list to a string with a space between each word
    new_phrase = ""
    for word in my_list:
        new_phrase += f"{word} "

    # Print out the updated phrase
    print(f"New phrase: {new_phrase}")

if __name__ == "__main__":
    main()