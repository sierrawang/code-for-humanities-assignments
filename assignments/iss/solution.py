import requests


def main():
    # Fetch the ISS location data from the API
    response = requests.get("https://api.wheretheiss.at/v1/satellites/25544")
    response_json = response.json()

    for key in response_json:
        print(f"{key}: {response_json[key]}")


if __name__ == '__main__':
    main()