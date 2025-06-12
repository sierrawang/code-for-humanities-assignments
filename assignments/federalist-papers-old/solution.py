import re
import math

# These are the papers where authorship is disputed
DISPUTED_PAPERS = [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 62, 63]

# Read a text file containing multiple Federalist Papers and returns a dictionary
# mapping each paper number to the name of its author.
# Each paper starts with a line like "Federalist No. X",
# and the author is always found on the line starting with "Author:".
#
# Parameters:
#     filename (str): The path to the text file containing the Federalist Papers.
#
# Returns:
#     dict: A dictionary where each key is an integer paper number (e.g., 1, 2, 3),
#             and each value is a string containing the name of the author (e.g., "Alexander Hamilton").
def load_authors_from_filename(filename):
    # Dictionary to store paper number -> author
    authors = {}            

    # Current paper number being processed 
    current_number = None
    
    with open(filename, 'r') as f:
        for line in f:
            stripped = line.strip()

            # Detect the start of a new paper
            if stripped.startswith("Federalist No."):
                try:
                    current_number = int(stripped.split("Federalist No.")[-1].strip())
                except ValueError:
                    current_number = None  # Skip if we can't extract a valid number

            # Detect the Author line and extract author's name
            elif stripped.startswith("Author:") and current_number is not None:
                author_name = stripped.split("Author:")[-1].strip()
                authors[current_number] = author_name
                current_number = None  # Reset to avoid mismatched entries

    return authors


# Read a text file containing multiple Federalist Papers and return a dictionary
# mapping each paper number to its full text. Assume each paper starts with a line 
# like "Federalist No. X",
# the actual content starts after the line that begins with "Author:",
# and ends at the line "PUBLIUS" or "PUBLIUS.".
#
# Parameters:
#     filename (str): The path to the text file containing the Federalist Papers.
#
# Returns:
#     dict: A dictionary where each key is an integer paper number (e.g., 1, 2, 3),
#             and each value is a string containing the full text of that paper.
def load_papers_from_filename(filename):
    # Dictionary to store paper number -> text
    papers = {}              
    
    # Current paper number being processed
    current_number = None    
    
    # Whether we're currently collecting the body of a paper
    collecting = False       
    
    # List to store lines of the current paper's text
    current_text = []        
    
    with open(filename, 'r', encoding='utf-8') as f:
        # Loop over every line in the file
        for line in f:
            stripped = line.strip()

            # Check if the line marks the start of a new paper
            if stripped.startswith("Federalist No."):
                # If we were already collecting a paper, save it
                if current_number is not None:
                    papers[current_number] = "\n".join(current_text).strip()
                
                # Get the paper number from the line
                try:
                    current_number = int(stripped.split("Federalist No.")[-1].strip())
                except ValueError:
                    current_number = None  # If we can't extract a number, skip this paper
                
                # Reset state for new paper
                current_text = []
                collecting = False
            
            elif stripped.startswith("Author:"):
                # Check if this line is the Author line

                # Start collecting text after this line
                collecting = True  
            
            elif collecting:
                # If we're in the body of a paper, collect lines
                current_text.append(line)

                # If we reach the end marker, stop collecting
                if stripped == "PUBLIUS" or stripped == "PUBLIUS.":
                    collecting = False
                    
                    # Save the completed paper
                    if current_number is not None:
                        papers[current_number] = "\n".join(current_text).strip()
                        current_number = None
                        current_text = []

    return papers

# Return a dictionary of each of the federalist papers 
# where the paper number is the key and the text is the value
def get_federalist_papers_dict_old(all_federalist_papers):
    parts = re.split(r'(FEDERALIST \d+)', all_federalist_papers)

    # Loop over the parts list and construct a dictionary
    # where the paper number is the key and the text is the value
    papers = parts[2::2]
    federalist_papers_dict = {}
    for i in range(len(papers)):
        federalist_papers_dict[i + 1] = papers[i]

    return federalist_papers_dict

# Return a dictionary of each of the federalist papers 
# where the paper number is the key and the text is the value
def get_federalist_papers_dict(all_text):
    papers_dict = {}
    lines = all_text.splitlines()

    current_paper_num = None
    current_paper_lines = []

    paper_header_pattern = re.compile(r"Federalist No\. (\d+)")
    
    for line in lines:
        header_match = paper_header_pattern.match(line.strip())
        if header_match:
            # Save the previous paper if it exists
            if current_paper_num is not None:
                papers_dict[current_paper_num] = "\n".join(current_paper_lines).strip()
            
            # Start new paper
            current_paper_num = int(header_match.group(1))
            current_paper_lines = [line]
        
        elif current_paper_num is not None:
            current_paper_lines.append(line)
    
    # Save the last paper
    if current_paper_num is not None:
        papers_dict[current_paper_num] = "\n".join(current_paper_lines).strip()
    
    return papers_dict

# Given a long string, return a list of all words
def tokenize(text):
    # Convert all non alphabetical characters to spaces
    clean_text = ""
    for ch in text:
        if ch.isalpha():
            clean_text += ch
        else:
            clean_text += " "

    # Convert the text to all lowercase
    clean_text = clean_text.lower()

    # Split the text by spaces
    word_list = clean_text.split()
    return word_list

# Convert the list of words to a dictionary with 
# the count of each word
def get_word_counts(word_list):
    word_counts = {}
    for word in word_list:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

# Build a probability model from a list of papers by a given author
def get_author_model(paper_numbers, federalist_papers_dict):
    # Construct a list of all words that the author has written
    all_words = []
    for num in paper_numbers:
        # Get a list of all words in this paper
        words = tokenize(federalist_papers_dict[num])

        # Add these words to the list
        all_words.extend(words)

    # Store the total number of words for this author
    total_words = len(all_words)

    # Get the counts per word
    word_counts = get_word_counts(all_words)

    # Convert each count to a probability (and add Laplace smoothing)
    probs = {word: (word_counts[word] + 1) / (total_words + len(word_counts)) for word in word_counts}
    
    return probs

# Calculate the log-likelihood ratio between Hamilton and Madison
def compute_log_likelihood_ratio(counts, p_probs, q_probs):
    log_ratio = 0.0

    # Loop over every word and its count in paper 49
    for word, count in counts.items():
        p = p_probs.get(word, 1e-12)
        q = q_probs.get(word, 1e-12)
        log_ratio += count * math.log(p / q)
    return log_ratio

# Construct a list of the papers that the given author wrote
def get_papers_by_author(federalist_papers_dict, authors_dict, author):
    # Initialize an empty list to hold the papers that this author wrote
    author_papers = []

    # Add the index of each paper that this author wrote
    for paper_num in federalist_papers_dict:
        if authors_dict[paper_num] == author:
            author_papers.append(paper_num)

    return author_papers

# Determine the most likely author of the disputed paper
def determine_author(federalist_papers_dict, authors_dict, paper_num):
    # Get the papers that each author is known to have written
    madison_papers = get_papers_by_author(federalist_papers_dict, authors_dict, "James Madison")
    hamilton_papers = get_papers_by_author(federalist_papers_dict, authors_dict, "Alexander Hamilton")

    # Build language models
    madison_model = get_author_model(madison_papers, federalist_papers_dict)
    hamilton_model = get_author_model(hamilton_papers, federalist_papers_dict)

    # Get disputed paper word frequencies
    disputed_paper_words = tokenize(federalist_papers_dict[paper_num])
    disputed_paper_counts = get_word_counts(disputed_paper_words)

    # Compute the log-likelihood ratio
    llr = compute_log_likelihood_ratio(disputed_paper_counts, madison_model, hamilton_model)

    if llr < 0:
        print(f"Hamilton is more likely to have written Paper {paper_num}.")
    elif llr > 0:
        print(f"Madison is more likely to have written Paper {paper_num}.")
    else:
        print(f"It is equally likely that either wrote Paper {paper_num}.")

def main():

    federalist_papers_dict = {}
    for i in range(8):
        lower_bound = 10 * i + 1
        upper_bound = (i + 1) * 10
        filename = f"papers/papers{lower_bound}-{upper_bound}.txt"
        tmp = load_papers_from_filename(filename)
        federalist_papers_dict.update(tmp)
            
    # Add the last file
    tmp = load_papers_from_filename(f"papers/papers81-85.txt")
    federalist_papers_dict.update(tmp)

    for key, item in federalist_papers_dict.items():
        print(key, item[:20], item[-10:])

    authors_dict = {}
    for i in range(8):
        lower_bound = 10 * i + 1
        upper_bound = (i + 1) * 10
        filename = f"papers/papers{lower_bound}-{upper_bound}.txt"
        tmp = load_authors_from_filename(filename)
        authors_dict.update(tmp)
            
    # Add the last file
    tmp = load_authors_from_filename(f"papers/papers81-85.txt")
    authors_dict.update(tmp)

    for key, item in authors_dict.items():
        print(key, item)

    # Determine who is more likely to have written paper 49
    paper_num = input("Enter the disputed paper number: ")
    while paper_num:
        paper_num = int(paper_num)
        determine_author(federalist_papers_dict, authors_dict, paper_num)
        paper_num = input("Enter the disputed paper number: ")

if __name__ == '__main__':
    main()
