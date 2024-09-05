import os

import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
phone_number = os.getenv("MY_PHONE_NUMBER")

client = Client(account_sid, auth_token)


class WeatherData:
    def __init__(self, city):
        self.params = {
            "id": city,
            "appid": API_KEY,
            "cnt": 4
        }
        self.end_point = "https://api.openweathermap.org/data/2.5/forecast"

    def get_weather(self):
        response = requests.get(url=self.end_point, params=self.params)
        response.raise_for_status()
        data = response.json()
        return data

    def umbrella_alert(self):
        data = self.get_weather()
        for weather in data["list"]:
            if weather["weather"][0]["id"] < 600:
                return "Bring an umbrella."
        return "No need for an umbrella."


def main():
    city = 3082707
    weather = WeatherData(city)
    print(weather.umbrella_alert())

    message = client.messages.create(
        from_=os.getenv("TWILIO_PHONE_NUMBER"),
        body=weather.umbrella_alert(),
        to=phone_number,
    )

    print(message.status)


if __name__ == '__main__':
    main()
