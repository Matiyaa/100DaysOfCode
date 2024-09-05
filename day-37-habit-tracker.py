import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()
PIXELA_ENDPOINT = os.getenv("PIXELA_ENDPOINT")
PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")


def create_user(token, username):
    user_params = {
        "token": token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
    print(response.text)


def create_graph(token, username):
    graph_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs"
    graph_config = {
        "id": "graph1",
        "name": "Coding Graph",
        "unit": "lines",
        "type": "int",
        "color": "ajisai"
    }
    headers = {
        "X-USER-TOKEN": token
    }
    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)


def add_pixel(token, username, quantity):
    pixel_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs/graph1"
    today = datetime.now().strftime("%Y%m%d")
    pixel_config = {
        "date": today,
        "quantity": quantity
    }
    headers = {
        "X-USER-TOKEN": token
    }
    response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
    print(response.text)


if __name__ == "__main__":
    if input("Do you want to create a user [y/n]? ") in ("yes", "y"):
        create_user(PIXELA_TOKEN, PIXELA_USERNAME)
        if input("Do you want to create a graph [y/n]? ") in ("yes", "y"):
            create_graph(PIXELA_TOKEN, PIXELA_USERNAME)
    if input("Do you want to add a pixel [y/n]? ") in ("yes", "y"):
        add_pixel(PIXELA_TOKEN, PIXELA_USERNAME, quantity=input("How many lines of code did you write today? "))
