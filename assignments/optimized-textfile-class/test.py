from optimized_text_file import OptimizedTextFile
import json


def exp_got(expected, got):
    print(f"Expected: {expected}, Got: {got}")
    print("Exiting...")
    quit()


doi = OptimizedTextFile("data/doi.txt")
sonnet5 = OptimizedTextFile("data/sonnet5.txt")
sonnet5sub = OptimizedTextFile("data/sonnet5sub.txt")

with open("solutions.json", "r") as f:
    solutions_dict = json.load(f)




given_dict = {}

given_dict["doi"] = {
    "line_count": doi.line_count,
    "word_count": doi.word_count,
    "char_count": doi.char_count,
    "count_word_the": doi.count_word("the"),
    "count_word_we": doi.count_word("we"),
    "lines_with_the": doi.get_lines_with_word("the"),
    "lines_with_we": doi.get_lines_with_word("we"),
    "get_common_lines_son5": doi.get_common_lines(sonnet5),
    "string_representation": str(doi),
}

given_dict["sonnet5"] = {
    "line_count": sonnet5.line_count,
    "word_count": sonnet5.word_count,
    "char_count": sonnet5.char_count,
    "count_word_the": sonnet5.count_word("the"),
    "count_word_we": sonnet5.count_word("we"),
    "lines_with_the": sonnet5.get_lines_with_word("the"),
    "lines_with_we": sonnet5.get_lines_with_word("we"),
    "get_common_lines_son5sub": sonnet5.get_common_lines(sonnet5sub),
    "string_representation": str(sonnet5),
}

given_dict["sonnet5sub"] = {
    "line_count": sonnet5sub.line_count,
    "word_count": sonnet5sub.word_count,
    "char_count": sonnet5sub.char_count,
    "count_word_the": sonnet5sub.count_word("the"),
    "count_word_we": sonnet5sub.count_word("we"),
    "lines_with_the": sonnet5sub.get_lines_with_word("the"),
    "lines_with_we": sonnet5sub.get_lines_with_word("we"),
    "get_common_lines_son5": sonnet5sub.get_common_lines(sonnet5),
    "string_representation": str(sonnet5sub),
}





for key in given_dict:
    for subkey in given_dict[key]:
        if subkey not in solutions_dict[key]:
            exp_got(f"Key '{subkey}' not found in solutions for '{key}'", given_dict[key][subkey])
        if given_dict[key][subkey] != solutions_dict[key][subkey]:
            print(f"Mismatch for '{subkey}' in '{key}'")
            exp_got(solutions_dict[key][subkey], given_dict[key][subkey])
        else:
            print(f"Success: {key}.{subkey} = {given_dict[key][subkey]}")
print("All tests passed successfully!")

