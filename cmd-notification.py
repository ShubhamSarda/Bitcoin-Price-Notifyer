#cmd Notification.

import requests
from bs4 import BeautifulSoup
import time

target_price = float(input("Enter Target Price - "))
#Input your Desired Price, loop will work till you reach Targeted price, 
#Once you at that point, it will break out of loop and Notify you. 

url = "https://ethereumprice.org/btc/"

while True:
    html = requests.get(url).text
    soup = BeautifulSoup(html,"lxml")
    current_price = soup.find("span",{"class":"rp"}).text
    price = current_price.replace(" ","").replace("$","").replace("\n","").replace(".","").replace(",","")
    aprice = float(price)/100
    if aprice > target_price:
        print(aprice)
        print("Target Achieved")
        time.sleep(6000)
        break
    print("Target Not Achieved, Current Price - "+ str(aprice))
    time.sleep(10)
