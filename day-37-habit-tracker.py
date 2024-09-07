import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()
PIXELA_ENDPOINT = os.getenv("PIXELA_ENDPOINT")
PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")
TODAY = datetime.now().strftime("%Y%m%d")


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
    pixel_config = {
        "date": TODAY,
        "quantity": quantity
    }
    headers = {
        "X-USER-TOKEN": token
    }
    response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
    print(response.text)


def update_pixel(token, username, quantity):
    pixel_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs/graph1/{TODAY}"
    pixel_config = {
        "quantity": quantity
    }
    headers = {
        "X-USER-TOKEN": token
    }
    response = requests.put(url=pixel_endpoint, json=pixel_config, headers=headers)
    print(response.text)


def delete_pixel(token, username):
    pixel_endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs/graph1/{TODAY}"
    headers = {
        "X-USER-TOKEN": token
    }
    response = requests.delete(url=pixel_endpoint, headers=headers)
    print(response.text)


def type_of_action(action):
    if action == "create_user":
        create_user(PIXELA_TOKEN, PIXELA_USERNAME)
    elif action == "create_graph":
        create_graph(PIXELA_TOKEN, PIXELA_USERNAME)
    elif action == "add_pixel":
        add_pixel(PIXELA_TOKEN, PIXELA_USERNAME, quantity=input("How many lines of code did you write today? "))
    elif action == "update_pixel":
        update_pixel(PIXELA_TOKEN, PIXELA_USERNAME, quantity=input("How many lines of code did you write today? "))
    elif action == "delete_pixel":
        delete_pixel(PIXELA_TOKEN, PIXELA_USERNAME)


if __name__ == "__main__":
    type_of_action(
        input("What would you like to do? (create_user, create_graph, add_pixel, update_pixel, delete_pixel): "))
