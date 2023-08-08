import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

API = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

# Email configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "akwaowoudokop15@gmail.com"
receiver_email = "akwaowoudokop15@gmail.com"
password = "bveaduvoezruunim"
target_price = 100

response = requests.get(API, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ("
                                                    "KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 "
                                                    "Edg/115.0.1901.188", "Accept-Language": "en-US,en;q=0.9 "
                                      })
amazon_webpage = response.text
# print(amazon_webpage)

soup = BeautifulSoup(amazon_webpage, "lxml")

item_price = soup.find(class_="a-offscreen").get_text()
item_price_without_currency = item_price.split("$")[1]
# print(price_without_currency)
item_price_as_float = float(item_price_without_currency)
# print(item_price_as_float)

if item_price_as_float < target_price:
    with smtplib.SMTP(smtp_server, smtp_port) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        message = f"Subject:Amazon Price Alert \n\n " \
                  f"Instant Pot Duo Plus 9-in-1 Electric Pressure Cooker, Slow Cooker, Rice Cooker, Steamer, Sauté, " \
                  f"Yogurt " \
                  f"Maker, Warmer & Sterilizer, Includes App With Over 800 Recipes, Stainless Steel, 3 Quart is now" \
                  f" ${item_price_as_float} \n " \
                  f"https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1 "
        message = message.encode('utf-8')
        connection.sendmail(from_addr=sender_email,
                            to_addrs=receiver_email,
                            msg=message)
