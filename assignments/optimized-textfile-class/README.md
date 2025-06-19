# Optimized Textfile class
In this assignment, you will implement a class called `OptimizedTextfile` in the `optimized_text_file.py` file. The specification for this class is below:

class name: `OptimizedTextfile`

Information passed to the constructor:
- `filename`: a string representing the name of the text file to be read.

attributes:
- `filename`: a string representing the name of the text file.
- `content`: a string containing the content of the text file.
- `lines`: a list of strings, where each string is a line from the text file.
- `word_count`: an integer representing the number of words in the text file. (note we count any non-whitespace sequence of characters as a word)
- `line_count`: an integer representing the number of lines in the text file.
- `char_count`: an integer representing the number of characters in the text file.


methods:
- `__init__(self, filename)`: Initializes the `OptimizedTextfile` object by reading the content of the file and calculating the attributes.
- `count_word(self, word)`: Returns the number of occurrences of a specific word in the text file.
- `get_lines_with_word(self, word)`: Returns a list of lines that contain a specific word.
- `get_common_lines(self, other)`: Returns a list of lines that are common between the current file and another `OptimizedTextfile` object.
- `__str__(self)`: Returns a string representation of the `OptimizedTextfile` object, that includes the first 10 characters of the content, then three dots.
    Example: `"This is th..."`

Implement the above methods in the order they are listed.

To check if your implementation is right, you can run the `test.py` file that is provided!


# Optional Extensions

Implement the following additional methods:
- `get_unique_words(self)`: Returns a set of unique words in the text file.
- `get_common_words(self, other)`: Returns a list of words that are common between the current file and another `OptimizedTextfile` object.
