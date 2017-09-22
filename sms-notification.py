#SMS Notification

from twilio.rest import Client
import requests
from bs4 import BeautifulSoup
import time

# Your Account SID from twilio.com/console
account_sid = "AC851844**************************"
# Your Auth Token from twilio.com/console
auth_token  = "0cbad**************************"

client = Client(account_sid, auth_token)

url = "https://ethereumprice.org/btc/"

target_price = float(input("Enter Target Price - "))
#Input your Desired Price, loop will work till you reach Targeted price, 
#Once you at that point, it will break out of loop and Notify you.


while True:
    html = requests.get(url).text
    soup = BeautifulSoup(html,"lxml")
    current_price = soup.find("span",{"class":"rp"}).text
    price = current_price.replace(" ","").replace("$","").replace("\n","").replace(".","").replace(",","")
    aprice = float(price)/100
    if aprice > target_price:
        message = client.messages.create(
            to="+91**********", #Your Mobile Number
            from_="+14*********", #Your Twilio Number
            body="Current BTC Price is - " + str(aprice))

        print(message.sid)
        time.sleep(6000)
        break
    print("Target Not Achieved, Current Price - "+ str(aprice))
    time.sleep(10)
