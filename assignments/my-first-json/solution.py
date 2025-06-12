import json

filename = "my_first.json"


def main():
    with open(filename, 'r') as file:
        data = json.load(file)
    
    
    for key in data:
        print(f"Key: {key}")
        print(f"Value: {data[key]}")


if __name__ == '__main__':
    main()