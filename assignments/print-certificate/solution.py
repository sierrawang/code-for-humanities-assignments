

def top():
    top_str = " "
    for i in range(10):
        top_str += "_"
    top_str += " "
    print(top_str)

def code_for_humanities():
    print("|Code 4 Hum|")

def middle():
    middle_str = "|"
    for i in range(10):
        middle_str += " "
    middle_str += "|"
    print(middle_str)


def filler(line_width):
    filler_str = "|"
    for i in range(line_width):
        filler_str += "-"
    for i in range(10 - line_width):
        filler_str += " "
    filler_str += "|"
    print(filler_str)


def bottom():
    top_str = "|"
    for i in range(10):
        top_str += "_"
    top_str += "|"
    print(top_str)

def main():
    # write your code here
    top()
    code_for_humanities()
    for i in range(6):
        filler(i)
    middle()
    bottom()

if __name__ == "__main__":
    main()