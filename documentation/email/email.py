import smtplib
import datetime as dt
import random

# Be kell állítani ez e-mail fiókot kisebb biztonságra, hogy alkalmazások használhassák. Amíg nem értesz hozzá, addig csak játszós e-mailt használj!!!
# Google Account/Settings/Securiy/Less Secure Acces On
MY_EMAIL = "Ide írd az e-mail címet, amivel küldöd"
PASSWORD = "Ide írd a jelszavad!"

now = dt.datetime.now()

with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="Ide írd a címzett e-mail címet", msg=f"Subject:Motivational Letter \n\n {quote}")
