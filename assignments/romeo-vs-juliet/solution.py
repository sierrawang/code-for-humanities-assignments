import matplotlib.pyplot as plt


def clean_word(word):
    new_word = ""
    for char in word:
        if char.isalpha():
            new_word += char
    return new_word

# EXTENSION 1:
def get_amount_of_speaking_parts(file_name):
    speaking_parts = {
        "ROMEO": 0,
        "JULIET": 0,
    }
    for line in open(file_name, "r"):
        if line.startswith("ROMEO"):
            speaking_parts["ROMEO"] += 1
        elif line.startswith("JULIET"):
            speaking_parts["JULIET"] += 1
    return speaking_parts

def get_amount_of_speaking_parts_any_character(file_name):
    speaking_parts = {}
    for line in open(file_name, "r"):
        if line.strip() == "":
            continue
        character_name = ""
        for char in line:
            if char.isalpha() and char.isupper():
                character_name += char
            elif char == " ":
                character_name += " "
            else:
                break
        if len(character_name.strip() ) > 1:
            character_name_list = character_name.split()
            
            for i in range(0, len(character_name_list)):
                if len(character_name_list[i]) < 2:
                    character_name = character_name_list[1]
            if character_name not in speaking_parts:
                speaking_parts[character_name] = 0
            speaking_parts[character_name] += 1

    return speaking_parts

def main():
    # Read in romeo_and_juliet.txt
    counts_dict = {}
    counts_dict["Romeo"] = 0
    counts_dict["Juliet"] = 0

    with open("romeo_and_juliet.txt", "r") as file:
        for line in file:
            # Print each line
            words = line.split()
            for word in words:
                cleaned_word = clean_word(word)
                if cleaned_word == "Romeo":
                    counts_dict["Romeo"] += 1
                elif cleaned_word == "Juliet":
                    counts_dict["Juliet"] += 1
    

    # make a bar chart
    plt.bar(counts_dict.keys(), counts_dict.values())
    plt.title("Romeo vs Juliet")
    plt.xlabel("Character")
    plt.ylabel("Number of Mentions")
    plt.savefig("romeo_vs_juliet.png")
    plt.show()


    # EXTENSION 1: Make a bar chart of the amount of speaking parts
    speaking_parts = get_amount_of_speaking_parts("romeo_and_juliet.txt")
    plt.bar(speaking_parts.keys(), speaking_parts.values())
    plt.title("Speaking Parts in Romeo and Juliet")
    plt.xlabel("Character")
    plt.ylabel("Number of Speaking Parts")
    plt.savefig("extension_1_expected_plot.png")
    plt.show()

    # EXTENSION 2: Make a bar chart of the amount of speaking parts for any character
    speaking_parts_any = get_amount_of_speaking_parts_any_character("romeo_and_juliet.txt")
    plt.bar(speaking_parts_any.keys(), speaking_parts_any.values())
    plt.title("Speaking Parts for Any Character in Romeo and Juliet")
    plt.xlabel("Character")
    plt.ylabel("Number of Speaking Parts")
    plt.xticks(rotation=90)  # Rotate x-axis labels for better readability

    plt.savefig("extension_2_expected_plot.png")
    plt.show()




if __name__ == "__main__":
    main()