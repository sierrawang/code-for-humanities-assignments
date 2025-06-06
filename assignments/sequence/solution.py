def main():
    # Get user input and convert to uppercase for consistency
    seq1 = input("Enter Sequence 1: ").upper()
    seq2 = input("Enter Sequence 2: ").upper()

    # Variables to keep track of the shift with the best match
    best_shift = 0
    max_matches = 0
    best_match_line = ""

    # Define the range of shifts: allow seq2 to slide fully over and past seq1 in both directions
    min_shift = -len(seq2) + 1
    max_shift = len(seq1)

    # Try out every possible shift and determine the best match
    for shift in range(min_shift, max_shift):
        match_count = 0
        match_line = ""

        # Loop over seq2 and compare it to the corresponding character in seq1 
        # (if within bounds)
        for i in range(len(seq2)):
            seq1_index = shift + i

            # Only compare if the index is within bounds of seq1
            if seq1_index >= 0 and seq1_index < len(seq1):
                if seq2[i] == seq1[seq1_index]:
                    # The characters match at this position
                    match_line += "|"
                    match_count += 1
                else:
                    # The characters do not match
                    match_line += " "

        # Update best match if this shift was better
        if match_count > max_matches:
            max_matches = match_count
            best_shift = shift
            best_match_line = match_line

    # Print the alignment
    print(f"Best alignment (shift = {best_shift}):")

    # Add spaces in between the characters of each string
    padded_line = " ".join(best_match_line)
    padded_seq1 = " ".join(seq1)
    padded_seq2 = " ".join(seq2)

    # Negative shift means pad sequence 1
    if best_shift < 0:
        for _ in range(0, -best_shift):
            padded_seq1 = f"  {padded_seq1}"
            padded_line = f"  {padded_line}"

    # Positive shift means pad sequence 2
    if best_shift > 0:
        for _ in range(0, best_shift):
            padded_seq2 = f"  {padded_seq2}"
            padded_line = f"  {padded_line}"
    
    # Print the display strings
    print(f"Sequence 1: {padded_seq1}")
    print(f"Sequence 2: {padded_seq2}")
    print(f"            {padded_line}")
    print(f"Matches: {max_matches}")

if __name__ == "__main__":
    main()
