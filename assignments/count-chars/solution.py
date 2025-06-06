def main():
    # Prompt the user to enter a phrase
    user_input = input("Enter a phrase: ")

    num_digits = 0
    num_letters = 0
    num_other = 0
    
    for char in user_input:
        if char.isdigit():
            num_digits += 1
        elif char.isalpha():
            num_letters += 1
        else:
            num_other += 1

    print(f"Your phrase had {num_digits} numbers, {num_letters} letters, and {num_other} other characters.")

if __name__ == "__main__":
    main()