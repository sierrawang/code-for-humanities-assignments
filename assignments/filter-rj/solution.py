

def main():
    lines = []
    with open("romeo_and_juliet.txt", 'r') as file:
        lines = file.readlines()
    
    # write lines to output file
    with open("output.txt", 'w') as output_file:
        for line in lines:
            if "Romeo" in line or "Juliet" in line:
                output_file.write(line.strip() + "\n")

if __name__ == '__main__':
    main()