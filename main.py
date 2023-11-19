import time
from tgtg import TgtgClient
import winsound

def check_availability(client, item_id):
    items = client.get_items(favorites_only=True)
    for item in items:
        if item['items_available'] > 0:
            return True
    return False


# Blow your ears out
duration = 100000  # milliseconds
freq = 440  # Hz


client = TgtgClient(email="123@gmail.com")
credentials = client.get_credentials()
access_token = credentials['access_token']
refresh_token = credentials['refresh_token']
user_id = credentials['user_id']
cookie = credentials['cookie']

email = "123@gmail.com"

client = TgtgClient(access_token=access_token, refresh_token=refresh_token, user_id=user_id, cookie=cookie)

ITEM_ID = '123'

while True:
    if check_availability(client, ITEM_ID):
        print("Found")
        winsound.Beep(freq, duration)
        break
    print("Waiting")
    time.sleep(10)