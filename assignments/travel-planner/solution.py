import os
import requests
from openai import OpenAI
import pandas as pd
from datetime import datetime

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
WEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

client = OpenAI(api_key = OPENAI_API_KEY)

# Fetch current weather for the specified city.
def get_city_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "imperial"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

# Fetch top news headlines for the specified city.
def get_city_news(city):
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "q": city,
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "pageSize": 5
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    articles = response.json().get("articles", [])
    return [article["title"] for article in articles]

# Use OpenAI API to generate travel suggestions and motivational quote.
def generate_ai_travel_tips(city, weather, news_headlines):
    headlines_formatted = "\n- ".join(news_headlines)
    prompt = (
        f"You are a friendly travel advisor. Given this city: {city}, its current weather: {weather}, "
        f"and some headlines:\n- {headlines_formatted}, generate:\n"
        "1. Three must-see places in the city\n"
        "2. One local food to try\n"
        "3. A motivational travel quote\n"
    )

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
    )

    text = response.choices[0].message.content.strip()
    sections = text.split("\n")
    result = {
        "Must-See Places": "\n".join(sections[0:3]),
        "Local Food": sections[3] if len(sections) > 3 else "",
        "Quote": sections[-1] if len(sections) > 4 else ""
    }
    return result

# ------------- Main Application Logic ------------- #

def main():
    print("Welcome to TravelBuddy AI!")
    city = input("Enter a city you'd like to visit: ").strip()

    try:
        weather_data = get_city_weather(city)
        weather_desc = weather_data['weather'][0]['description'].capitalize()
        temp = weather_data['main']['temp']
        weather_summary = f"{weather_desc}, {temp}°F"

        news = get_city_news(city)
        tips = generate_ai_travel_tips(city, weather_summary, news)

        # Prepare data for saving
        trip_data = {
            "City": city,
            "Date": datetime.now().strftime("%Y-%m-%d"),
            "Weather": weather_summary,
            "Top News Headlines": " | ".join(news),
            "Must-See Places": tips["Must-See Places"],
            "Local Food": tips["Local Food"],
            "Motivational Quote": tips["Quote"]
        }

        df = pd.DataFrame([trip_data])
        filename = f"trip_plan_{city.lower().replace(' ', '_')}.csv"
        df.to_csv(filename, index=False)

        # Display summary to user
        print("\n------ Your Travel Plan ------")
        print(f"Destination: {trip_data['City']}")
        print(f"Weather: {trip_data['Weather']}")
        print("Top News:")
        for headline in news:
            print(f" - {headline}")
        print("\nAI Recommendations:")
        print(f"Must-See Places:\n{tips['Must-See Places']}")
        print(f"Local Food: {tips['Local Food']}")
        print(f"Quote: {tips['Quote']}")
        print(f"\n📁 Trip plan saved to {filename}")

    except requests.HTTPError as e:
        print(f"API Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()