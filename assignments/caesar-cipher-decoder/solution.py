
MOST_COMMONLY_USED_LETTERS = [
    'e', 't', 'a', 'o', 'i'
]

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def get_encrypted_message():
    filename = "message.txt"
    with open(filename, 'r') as file:
        encrypted_message = file.read().strip()
    return encrypted_message

def main():
    encrypted_message = get_encrypted_message()
    character_counts = {}
    for character in encrypted_message:
        if not character.isalpha():
            continue
        
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1

    top_five_characters = []

    for i in range(5):
        largest_char = ""
        largest_count = 0
        for character in character_counts:
            if character_counts[character] > largest_count:
                largest_char = character
                largest_count = character_counts[character]
        
        character_counts[largest_char] = 0
        top_five_characters.append(largest_char)

    for i in range(5):
        encrypted_letter = top_five_characters[i]
        common_letter = MOST_COMMONLY_USED_LETTERS[i]
        shift = ord(encrypted_letter) - ord(common_letter)
        decrypted_message = ""
        for char in encrypted_message:
            if not char.isalpha():
                decrypted_message += char
            else:
                decrypted_message += ALPHABET[(ALPHABET.index(char) - shift)%26]
        print(decrypted_message)
        










if __name__ == '__main__':
    main()
