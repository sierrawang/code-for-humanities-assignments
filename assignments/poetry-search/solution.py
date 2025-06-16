import requests

# URL = https://poetrydb.org/author,title/Shakespeare;Sonnet
BASE_URL = "https://poetrydb.org/"


def parse_and_print_poems(resp_json):
    print(f"Found {len(resp_json)} poems.")
    for i in range(5):
        if i >= len(resp_json):
            break
        poem = resp_json[i]
        print(f"\nTitle: {poem.get('title', 'No title')}")
        print(f"Author: {poem.get('author', 'No author')}")
        print("Lines:")
        for line in poem.get('lines', []):
            print(f"  {line}")

def main():
    author = input("Enter the author's name: ")
    title = input("Enter the poem's title: ")
    if not author and not title:
        print("Either an author or title are required.")
    elif author and title:
        url = f"{BASE_URL}author,title/{author};{title}"
        response = requests.get(url)
        parse_and_print_poems(response.json())
    elif author:
        url = f"{BASE_URL}author/{author}"
        response = requests.get(url)
        parse_and_print_poems(response.json())
    elif title:
        url = f"{BASE_URL}title/{title}"
        response = requests.get(url)
        parse_and_print_poems(response.json())


if __name__ == '__main__':
    main()