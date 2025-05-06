alphabet = 'abcdefghijklmnopqrstuvwxyz'

def main():
    message_to_encrypt = input("Enter a message: ")
    shift_number = input("Enter a shift number: ")
    # Check if shift_number is a number
    if not shift_number.isdigit():
        print("Shift number must be a number.")
        return
    shift_number = int(shift_number)
    encrypted_message = ""
    for char in message_to_encrypt:
        if char.isalpha():
            # Check if character is uppercase
            if char.isupper():
                index = alphabet.index(char.lower())
                new_index = (index + shift_number) % 26
                encrypted_message += alphabet[new_index].upper()
            else:
                index = alphabet.index(char)
                new_index = (index + shift_number) % 26
                encrypted_message += alphabet[new_index]
        else:
            encrypted_message += char
    print("Encrypted message:", encrypted_message)




if __name__ == '__main__':
    main()