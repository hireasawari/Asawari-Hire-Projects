import requests
from twilio.rest import Client

url="https://api.openweathermap.org/data/2.5/forecast"
appid="TWILIO APPID"
account_sid="TWILIO ACC SID"

auth_token="AUTH TOKEN"

parameters={
    "lat":45.997454,
    "lon":73.734345,
    "appid":appid,
    "cnt": 4
}

response=requests.get(url=url,params=parameters)
response.raise_for_status()
data=response.json()
weather_id=data["list"][0]["weather"][0]["id"]
print(weather_id)


if 200<weather_id<232 :
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"It's a thunderstorm 🌩️ . Stay Home , Stay safe.🏠",
        from_='TWILIO PHONE NO.',
        to='NO. TO WHICH MSG TO BE SENT'
    )

    print(message.status)

elif 300<weather_id<322 :
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"Today will be a light rain drizzle 🌧️.Remember to keep an umbrella ☂️.",
        from_='TWILIO PHONE NO.',
        to='NO. TO WHICH MSG TO BE SENT'
    )

    print(message.status)

elif 500<weather_id<532 :
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"Chances of high rain today ⛈️.Remember to keep an umbrella ☂️.",
        from_='TWILIO PHONE NO.',
        to='NO. TO WHICH MSG TO BE SENT'
    )

    print(message.status)

elif 600<weather_id<632 :
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"Snow is expected today! ❄️ Stay warm and carry an umbrella ☂️.",
        from_='TWILIO PHONE NO.',
        to='NO. TO WHICH MSG TO BE SENT'
    )

    print(message.status)


else:
    print("no rain")
