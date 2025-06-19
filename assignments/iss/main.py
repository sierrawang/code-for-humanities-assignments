import requests

def main():
    iss_url = "https://api.wheretheiss.at/v1/satellites/25544"

    response = requests.get(iss_url)
    response_data = response.json()

    for key in response_data:
        print(f"{key}: {response_data[key]}")



if __name__ == '__main__':
    main()