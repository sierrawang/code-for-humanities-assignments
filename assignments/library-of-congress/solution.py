import requests
import json

def main():
    URL = "https://chroniclingamerica.loc.gov/search/titles/results"
    params = {
        "terms": "car",
        "format": "json",
        "page": 1,
    }

    response = requests.get(URL, params=params)
    data = response.json()
    print(len(data["items"]), "items found.")
    for key in data["items"]:
        print(f"Title: {key['title']}")

if __name__ == '__main__':
    main()
