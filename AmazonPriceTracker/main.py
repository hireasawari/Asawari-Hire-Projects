from bs4 import BeautifulSoup
import requests
from twilio.rest import Client

# Product URL
URL = "https://appbrewery.github.io/instant_pot/"


# Function to get price from the website
def get_price():
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract price
    price_tag = soup.find(name="span", class_="a-offscreen")
    if price_tag:
        price = float(price_tag.text.strip().replace("$", ""))
        return price
    return None


# Function to send email if price drops
def send_msg(price):
    account_sid = "ACC_SID"
    auth_token = "AUTH_TOKEN"
    subject = "🔥 Price Drop Alert! 🔥"
    URL = "https://appbrewery.github.io/instant_pot/"

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"Subject: {subject}\n\nThe Instant Pot is now available for ${price}!\nBuy now: {URL}",
        from_='TWILIO_NO.',
        to='N0. WHERE MSG TO BE SENT'
    )

# Check price and send email if condition is met
current_price = get_price()
print(current_price)
if current_price and current_price <= 99.99:
    send_msg(current_price)
    print("Message sent successfully!!")
else:
    print(f"Current price (${current_price}) is still above the threshold.")
