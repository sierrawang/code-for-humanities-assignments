import requests

BASE_URL = "https://techy-api.vercel.app/api/json"

def main():
    response = requests.get(BASE_URL)
    data = response.json()
    print(data["message"])


if __name__ == '__main__':
    main()