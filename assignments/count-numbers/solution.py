

def main():
    counter = {}
    with open("numbers.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line in counter:
                counter[line] += 1
            else:
                counter[line] = 1
    
    for count in counter:
        print(f"{count} appears {counter[count]} times")




if __name__ == "__main__":
    main()