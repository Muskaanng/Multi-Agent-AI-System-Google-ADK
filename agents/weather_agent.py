import requests
import os

class WeatherAgent:
    def get_weather(self, launch_data):
        lat = launch_data.get("latitude")
        lon = launch_data.get("longitude")
        if not lat or not lon:
            return {"error": "Invalid coordinates for weather lookup"}

        api_key = os.getenv("OPENWEATHER_API_KEY")
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                "location": launch_data.get("location"),
                "temperature": data["main"]["temp"],
                "weather": data["weather"][0]["description"],
                "wind_speed": data["wind"]["speed"]
            }
        else:
            return {"error": "Failed to fetch weather data"}