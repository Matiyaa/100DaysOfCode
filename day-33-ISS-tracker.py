from datetime import datetime

import requests

MY_LAT = 50.765884  # My latitude
MY_LONG = 16.282534  # My longitude

iss_location = requests.get(url='http://api.open-notify.org/iss-now.json')
iss_location.raise_for_status()

data = iss_location.json()

longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

iss_position = (longitude, latitude)

parameters = {
    'lat': MY_LAT,
    'lng': MY_LONG,
    'formatted': 0
}

info = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
info.raise_for_status()
sunrise = info.json()['results']['sunrise'].split('T')[1].split(':')[0]
sunset = info.json()['results']['sunset'].split('T')[1].split(':')[0]

time_now = datetime.now().hour

if int(sunset) < time_now < int(sunrise):
    if MY_LAT - 5 <= float(latitude) <= MY_LAT + 5 and MY_LONG - 5 <= float(longitude) <= MY_LONG + 5:
        print('Look up! The ISS is above you!')
    else:
        print('The ISS is not above you.')
else:
    print("It's daytime. You can't see the ISS.")
