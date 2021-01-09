import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

def OTPGen():
    otp=random.randint(10000,99999)
    return otp

def otpSendViaMail(email,message):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("YOUR_EMAIL","YOUR_PASSWORD")
    message = """\
        Subject: Hi there
        This message is sent from Demo ."""
    server.sendmail("YOUR_EMAIL",email,message)
    server.quit()

