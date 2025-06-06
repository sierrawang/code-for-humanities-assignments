def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    
    correct_answer_count = 0
    for word_to_translate in translations:
        user_answer = input(f"What is the Spanish translation for {word_to_translate}?")
        correct_answer = translations[word_to_translate]
        if user_answer == correct_answer:
            print("That is correct!")
            correct_answer_count += 1
        else:
            print(f"That is incorrect, the Spanish translation for {word_to_translate} is {correct_answer}.")
        print()
    print(f"You got {correct_answer_count}/{len(translations)} words correct, come study again soon!")





if __name__ == '__main__':
    main()