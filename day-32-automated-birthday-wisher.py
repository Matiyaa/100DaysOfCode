import datetime as dt
import os
import random
import smtplib

import pandas as pd

target_email = ''
letter_templates = 'day-32-data/letter_templates'

with open('email-app-pass.txt') as file:
    lines = file.readlines()
    my_email = lines[0].strip()
    my_password = lines[1].strip()

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
