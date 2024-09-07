import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()
NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")
NUTRITIONIX_ENDPOINT = os.getenv("NUTRITIONIX_ENDPOINT")
GENDER = os.getenv("GENDER")
WEIGHT_KG = os.getenv("WEIGHT_KG")
HEIGHT_CM = os.getenv("HEIGHT_CM")
AGE = os.getenv("AGE")
CURRENT_DATE = datetime.now().strftime("%d/%m/%Y")
CURRENT_TIME = datetime.now().strftime("%H:%M:%S")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")


def get_exercise_data(exercise):
    exercise_endpoint = f"{NUTRITIONIX_ENDPOINT}"
    headers = {
        "x-app-id": NUTRITIONIX_APP_ID,
        "x-app-key": NUTRITIONIX_API_KEY
    }
    exercise_params = {
        "query": exercise,
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE
    }
    response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
    return response.json()


def add_exercise_data(exercise_data):
    sheety_params = {
        "workout": {
            "date": CURRENT_DATE,
            "time": CURRENT_TIME,
            "exercise": exercise_data["name"].title(),
            "duration": exercise_data["duration_min"],
            "calories": exercise_data["nf_calories"]
        }
    }
    headers = {
        "Authorization": f"Bearer {SHEETY_TOKEN}"
    }
    response = requests.post(url=SHEETY_ENDPOINT, json=sheety_params, headers=headers)
    print(response.text)


if __name__ == "__main__":
    results = get_exercise_data(input("Tell me which exercise you did: "))
    for exercise in results["exercises"]:
        add_exercise_data(exercise)
