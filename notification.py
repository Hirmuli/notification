from notifypy import Notify
import requests
import schedule
import time

def func():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    notification = Notify()

    notification.title = "Price update"
    notification.message = "Bitcoins current price: "  +  data["bpi"]["USD"]["rate"] + " $ / " + data["bpi"]["EUR"]["rate"] + " €"

    notification.send()


schedule.every(1).minutes.do(func)

while True:
    schedule.run_pending()
    time.sleep(1)
