import datetime as dt
import os
import random
import smtplib

import pandas as pd
from dotenv import load_dotenv

load_dotenv()

target_email = ''
letter_templates = 'day-32-data/letter_templates'

my_email = os.getenv('MY_EMAIL')
my_password = os.getenv('MY_PASS')

if target_email == '':
    target_email = my_email

now = dt.datetime.now()

if now.weekday() == 0:
    with open('day-32-quotes.txt') as file:
        message = file.readlines()
        message = random.choice(message)

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=target_email,
                            msg=f'Subject:Get Motivated!\n\n{message}')

birthdays = pd.read_csv('day-32-data/birthdays.csv')

for birthday in birthdays.itertuples(index=False):
    if (birthday.day == now.day) and (birthday.month == now.month):
        with open(letter_templates + '/' + random.choice(os.listdir(letter_templates))) as file:
            message = file.read()
            message = message.replace('[NAME]', birthday.name)

        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=birthday.email,
                                msg=f'Subject:Happy Birthday {birthday.name}!\n\n{message}')
