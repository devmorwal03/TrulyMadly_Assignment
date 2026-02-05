import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather(city):
    key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric"
    data = requests.get(url).json()

    if "main" not in data:
        return {"error": "City not found"}

    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "weather": data["weather"][0]["description"]
    }