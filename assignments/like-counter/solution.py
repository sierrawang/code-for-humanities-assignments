def count_likes(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    for line in lines:
        stripped_line = line.strip()
        if stripped_line == "":
            continue

        # Split the line into words
        words = stripped_line.split()

        like_count = 0
        # Count occurrences of "like"
        for word in words:
            if "like" in word:
                like_count += 1

        # Extract the student's name (before the colon)
        student_name = line.split(":")[0]

        # Print the result
        print(f"{student_name} said 'like' {like_count} times.")


def main():
    file_path = "weekend_stories.txt"
    count_likes(file_path)


if __name__ == "__main__":
    main()
