import os
import matplotlib.pyplot as plt

def get_clean_text(text):
    clean_text = ""
    for ch in text:
        if ch.isalpha() or ch == " ":
            clean_text += ch
    return clean_text

# Count the occurrences of the term in the text
def count_term_in_text(text, term):
    text = get_clean_text(text)
    words = text.split()
    term = term.lower()
    count = 0
    for word in words:
        if word == term:
            count += 1
    return count

# Update the count for the given decade in the given dictionary
def add_count_to_decade(counts_per_decade, decade, count):
    if decade in counts_per_decade:
        counts_per_decade[decade] += count
    else:
        counts_per_decade[decade] = count

# Return True if the given filename is a "Notes" file
def is_notes_file(name):
    return "Notes" in name

# Parse the year from the name
def get_year_from_filename(name):
    # Split the file name into parts
    # and grab the last element
    parts = name.split("_")
    year = parts[-1]

    # Remove the "a" or "c" at the end (if it exists)
    if len(year) > 4:
        year = year[:4]

    return year

# Get the decade (int) from the given year (string)
# For ex, given "2015", return 2010
def get_decade(year):
    year = int(year)
    decade = (year // 10) * 10
    return int(decade)

def main():    
    # Ask the user what term they would like to search
    term = input("Enter the term to search for: ")

    # Initialize a dictionary to store the counts of the term
    # per decade
    counts_per_decade = {}

    # Loop over every file in the transcriptions folder,
    # count the occurrences of the term in that file,
    # and update the result dictionary
    for filename in os.listdir("transcriptions"):
        # Remove ".txt" from the filename
        name = filename[:-4]

        # Skip the notes files
        if is_notes_file(name):
            continue

        # Parse the year from the name
        year = get_year_from_filename(name)

        # Convert the year to the decade (for a prettier graph)
        decade = get_decade(year)

        # Read the contents of the file 
        with open(os.path.join("transcriptions", filename), encoding='latin_1', errors='ignore') as f:
            text = f.read()

            # Count the instances of the term in the file text
            count = count_term_in_text(text, term)

            # Update the counts dictionary
            add_count_to_decade(counts_per_decade, decade, count)

    print(counts_per_decade)

    # Construct the sorted decades and counts lists for graphing
    decades = list(counts_per_decade.keys())
    decades.sort()
    counts = []
    for decade in decades:
        counts.append(counts_per_decade[decade])

    # Plot
    plt.figure(figsize=(8,4))
    plt.plot(decades, counts, marker="o", linestyle="-", color='purple')
    plt.title(f"Occurrences of '{term}' Over Time")
    plt.xlabel("Decade")
    plt.ylabel("Num Occurrences")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

