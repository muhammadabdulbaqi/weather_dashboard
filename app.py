import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
API_KEY = os.getenv("WEATHER_API_KEY")

BASE_URL = "https://api.weatherapi.com/v1/current.json"

def get_weather(city):
    try:
        params = {
            "key": API_KEY,
            "q": city
        }
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    city = input("Enter a city name: ")
    weather = get_weather(city)
    if weather:
        print(f"Weather in {city}: {weather['current']['temp_c']}°C")
        print(f"Description: {weather['current']['condition']['text']}")
