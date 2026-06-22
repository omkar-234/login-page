import smtplib
from email.message import EmailMessage

# Dummy User as
USERNAME = "admin"
PASSWORD = "admin123"

MAX_ATTEMPTS = 4
attempts = 0


def send_email():

    sender = "omkarbachche8022@gmail.com"
    receiver = "omkarbachche8022@gmail.com"

    msg = EmailMessage()
    msg["Subject"] = "Account Locked Alert"
    msg["From"] = sender
    msg["To"] = receiver

    msg.set_content("""
User Account Locked.

Reason:
4 Failed Login Attempts Detected.

Server: EC2 Login Application
""")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, "paar qvnw vaeq shps")
        smtp.send_message(msg)


while attempts < MAX_ATTEMPTS:

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == USERNAME and password == PASSWORD:
        print("\nLogin Successful")
        break

    else:
        attempts += 1

        if attempts < MAX_ATTEMPTS:
            print(f"\nWrong Password! Attempt {attempts}/3")

if attempts == MAX_ATTEMPTS:

    print("\nAccount Locked")
    send_email()
