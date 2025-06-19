

# TODO: Fill in the specified methods and attributes below!
class OptimizedTextFile:
    def __init__(self, filename):
        self.filename = filename
        self.lines = []
        self.line_count = 0
        self.word_count = 0
        self.char_count = 0

        with open(filename, 'r') as file:
            for line in file:
                self.lines.append(line.rstrip('\n'))
                self.line_count += 1

                self.char_count += len(line)
                words = line.split()
                self.word_count += len(words)

    def clean_word(self, word):
        # Init a clean word string
        clean_word = ""

        # Add each letter of the word to the result
        for ch in word:
            if ch.isalpha():
                clean_word += ch

        # Make the clean word lowercase
        clean_word = clean_word.lower()

        return clean_word
    
    def count_word(self, word):
        clean_word = self.clean_word(word)
        count = 0
        for line in self.lines:
            words = line.lower().split()
            for unclean_word in words:
                if self.clean_word(unclean_word) == clean_word:
                    count += 1
        return count
    
    def get_lines_with_word(self, word):
        clean_word = self.clean_word(word)
        lines_with_word = []
        for line in self.lines:
            words = line.lower().split()
            for unclean_word in words:
                if self.clean_word(unclean_word) == clean_word:
                    lines_with_word.append(line)
                    break
        return lines_with_word
    

    def get_common_lines(self, other):
        common_lines = []
        for line in self.lines:
            if line in other.lines:
                common_lines.append(line)
        return common_lines
    
    def __str__(self):
        start_str = ""
        for line in self.lines:
            for char in line:
                start_str += char
                if len(start_str) >= 10:
                    return f"{start_str}..."
        return start_str if start_str else "No content"