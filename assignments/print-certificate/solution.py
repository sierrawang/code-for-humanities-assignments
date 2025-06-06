import random

def top(line_width=10):
    top_str = " "
    for i in range(line_width):
        top_str += "_"
    top_str += " "
    print(top_str)

def code_for_humanities(line_width=10):
    code_str = "|"
    code_str += "C4H"
    for i in range(line_width - 3):
        code_str += " "
    code_str += "|"
    print(code_str)

def middle(line_width=10):
    middle_str = "|"
    for i in range(line_width):
        middle_str += " "
    middle_str += "|"
    print(middle_str)


def filler(dash_length, line_width=10):
    filler_str = "|"
    for i in range(dash_length):
        filler_str += "-"
    for i in range(line_width - dash_length):
        filler_str += " "
    filler_str += "|"
    print(filler_str)


def bottom(line_width=10):
    top_str = "|"
    for i in range(line_width):
        top_str += "_"
    top_str += "|"
    print(top_str)

def main():
    # write your code here
    line_width = 10
    top(line_width)
    code_for_humanities(line_width)
    filler(8, line_width)
    filler(9, line_width)
    filler(8, line_width)
    filler(9, line_width)
    filler(8, line_width)
    middle(line_width)
    bottom(line_width)

if __name__ == "__main__":
    main()