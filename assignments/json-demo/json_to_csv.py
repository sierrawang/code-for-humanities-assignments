import json
import os

def main():
    # Initialize resulting dictionary
    result = {
        "title": [],
        "pages": [],
        "ID": []
    }

    # Loop through all of the files in the json files folder
    for filename in os.listdir("json_files"):
        # Load the contents of each file

    # Output the result to a csv

if __name__ == '__main__':
    main()