import requests

API_KEY = "your api key here"  # Replace with your actual API key
URL = "https://api.nasa.gov/planetary/apod"

def main():
    response = requests.get(
        URL,
        params={
            "api_key": API_KEY
        }
    )
    # save response as an image
    resp_json = response.json()
    
    image_url = resp_json.get("url")
    if image_url:
        image_response = requests.get(image_url)
        with open("apod_image.jpg", "wb") as file:
                file.write(image_response.content)
    else:
        print("No image URL found in the response.")


if __name__ == '__main__':
    main()