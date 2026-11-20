import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")


def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if response.status_code == 200:
            print("\n===== CURRENT WEATHER =====")
            print("City:", data["name"])
            print("Temperature:", data["main"]["temp"], "°C")
            print("Feels Like:", data["main"]["feels_like"], "°C")
            print("Humidity:", data["main"]["humidity"], "%")
            print("Weather:", data["weather"][0]["description"])
            print("Wind Speed:", data["wind"]["speed"], "m/s")

        elif response.status_code == 401:
            print("API key is not active yet. Please try again later.")

        elif response.status_code == 404:
            print("City not found. Please enter a valid city name.")

        else:
            print("Something went wrong:", data.get("message"))

    except requests.exceptions.RequestException:
        print("Network error. Please check your internet connection.")



def get_forecast(city):
    url = "https://api.openweathermap.org/data/2.5/forecast"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if response.status_code == 200:
            print("\n===== 5-DAY WEATHER FORECAST =====")

            shown_dates = set()

            for item in data["list"]:
                date = item["dt_txt"].split(" ")[0]

                if date not in shown_dates:
                    shown_dates.add(date)

                    print("\nDate:", date)
                    print("Temperature:", item["main"]["temp"], "°C")
                    print("Weather:", item["weather"][0]["description"])
                    print("Humidity:", item["main"]["humidity"], "%")

                    if len(shown_dates) == 5:
                        break

        else:
            print("Forecast Error:", data.get("message"))

    except requests.exceptions.RequestException:
        print("Network error while fetching forecast.")

print("===== WEATHER APP =====")

city = input("Enter city name: ")

get_weather(city)
get_forecast(city)