def main():
    # Define my_list
    my_list = ["I", "love", "to", "code", "!"]
    
    # Initialize an empty list
    new_list = []

    # Copy the contents of my_list to new_list
    for word in my_list:
        new_list.append(word)

    # Print the new list
    print(f"New list: {new_list}")

if __name__ == "__main__":
    main()