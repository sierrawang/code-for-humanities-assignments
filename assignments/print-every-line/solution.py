

def main():
    filename = "poem.txt"

    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())
    
if __name__ == '__main__':
    main()