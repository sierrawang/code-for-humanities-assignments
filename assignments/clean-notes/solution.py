def clean_text_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    cleaned_lines = []
    for line in lines:
        stripped_line = line.strip()
        if stripped_line != "":
            cleaned_lines.append(stripped_line)

    for line in cleaned_lines:
        print(line)

def main():
    clean_text_file("messy_text.txt")

if __name__ == "__main__":
    main()
