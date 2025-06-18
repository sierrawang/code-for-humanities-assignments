import requests

URL = "https://api.sunrise-sunset.org/json"

def main():
    lattitude = input("Enter the latitude: ")
    longitude = input("Enter the longitude: ")
    params = {
        "lat": lattitude,
        "lng": longitude,
        "tzid": "America/Los_Angeles",  # You can change this to your desired timezone
    }
    response = requests.get(URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["status"] == "OK":
            print(f"Sunrise: {data['results']['sunrise']}")
            print(f"Sunset: {data['results']['sunset']}")
        else:
            print("Error:", data["status"]) 


if __name__ == '__main__':
    main()