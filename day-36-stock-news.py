import os

import requests
from dotenv import load_dotenv
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
load_dotenv()


def get_stock_data():
    api_key = os.getenv("ALPHAVANTAGE_API_KEY")
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={api_key}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data


def get_stock_price(data):
    time_series = data["Time Series (Daily)"]
    time_series_list = [value for (key, value) in time_series.items()]
    yesterday_data = time_series_list[0]
    day_before_yesterday_data = time_series_list[1]
    yesterday_closing_price = float(yesterday_data["4. close"])
    day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])
    return yesterday_closing_price, day_before_yesterday_closing_price


def get_news():
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={api_key}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data


def send_sms(message):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        from_=os.getenv("TWILIO_PHONE_NUMBER"),
        to=os.getenv("MY_PHONE_NUMBER")
    )
    print(message.status)


def main():
    stock_data = get_stock_data()
    yesterday_closing_price, day_before_yesterday_closing_price = get_stock_price(stock_data)
    price_difference = yesterday_closing_price - day_before_yesterday_closing_price
    price_difference_percent = round((price_difference / yesterday_closing_price) * 100)
    news_data = get_news()
    headline = news_data["articles"][0]["title"]
    brief = news_data["articles"][0]["description"]
    if price_difference_percent > 0:
        emoji = "🔺"
    else:
        emoji = "🔻"
    message = f"{STOCK}: {emoji}{price_difference_percent}%\nHeadline: {headline}\nBrief: {brief}"
    send_sms(message)


if __name__ == "__main__":
    main()
