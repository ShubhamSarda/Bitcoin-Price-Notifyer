#Email Notification

import requests
from bs4 import BeautifulSoup
import time
import smtplib 

host = "smtp.gmail.com"
port = 587
username = str("*********@gmail.com") #Email Address Which You Need To Use To Send Mail.
password = str("************") #Password

from_email = username
to_email = "*********@gmail.com" #Email Address Where You Want To Send Notification.

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
        message = "Target Achieved, Current Price - "+ str(aprice)
        email_conn = smtplib.SMTP(host,port)
        email_conn.ehlo()
        email_conn.starttls()
        email_conn.login(username,password)
        email_conn.sendmail(from_email, to_email, message)
        email_conn.quit()
        time.sleep(6000)
        break
    print("Target Not Achieved, Current Price - "+ str(aprice))
    time.sleep(10)
