
# MOST_COMMONLY_USED_LETTERS contains the top 5 most commonly used letters in the English language (in order)
MOST_COMMONLY_USED_LETTERS = [ 'e', 't', 'a', 'o', 'i' ]
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def get_encrypted_message():
    filename = "message.txt"
    with open(filename, 'r') as file:
        encrypted_message = file.read().strip()
    return encrypted_message

def main():
    encrypted_message = get_encrypted_message()
    # TODO: Write your code here


if __name__ == '__main__':
    main()
