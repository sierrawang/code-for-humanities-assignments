def extract_on_the_record(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    on_the_record = False
    for line in lines:
        stripped_line = line.strip()

        if stripped_line == "ON THE RECORD":
            on_the_record = True
            continue
        elif stripped_line == "OFF THE RECORD":
            on_the_record = False
            continue

        if on_the_record:
            print(line.strip())


def main():
    # Specify the path to the text file
    file_path = "interview_transcript.txt"

    # Call the function to extract "on the record" lines
    extract_on_the_record(file_path)


if __name__ == "__main__":
    main()
