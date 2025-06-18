import requests

def main():
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    response = requests.get(url)
    response_json = response.json()

    for key in response_json:
        print(f"{key}: {response_json[key]}")


if __name__ == '__main__':
   main()
