

def main():
    filename = "poem.txt"
    
    with open(filename, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                print(str(line))
                break

if __name__ == '__main__':
    main()