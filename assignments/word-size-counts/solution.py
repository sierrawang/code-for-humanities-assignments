


def get_text():
    # Read ./data/romeo_and_juliet.txt
    with open("./data/romeo_and_juliet.txt", "r") as file:
        text = file.read()
    return text


def main():
    romeo_and_juliet = get_text()
    all_words = romeo_and_juliet.split()
    all_word_sizes = {}
    for word in all_words:
        word_size = len(word)
        if word_size in all_word_sizes:
            all_word_sizes[word_size] += 1
        else:
            all_word_sizes[word_size] = 1
    
    for i in range(1, 11):
        if i in all_word_sizes:
            print(f"Words of size {i}: {all_word_sizes[i]}")
        else:
            print(f"Words of size {i}: 0")



if __name__ == "__main__":
    main()