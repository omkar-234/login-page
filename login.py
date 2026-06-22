import smtplib
from email.message import EmailMessage

USERNAME = "admin"
PASSWORD = "admin123"

username = "admin"
password = "admin123"

if username == USERNAME and password == PASSWORD:
    print("Login Successful")
else:
    print("Invalid Login")
