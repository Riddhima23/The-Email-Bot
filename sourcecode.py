import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
import json

listener = sr.Recognizer()
bot=pyttsx3.init()
bot. setProperty("rate", 155)

def talk(text):
    bot.say(text)
    bot.runAndWait()
def get_info():
    try:
        with sr.Microphone() as source:
            print('Go ahead....')
            voice=listener.listen(source)
            info=listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        talk('Sorry Couldnt catch that!')   
def send_email(sender, pwd, receiver, subject, body):
    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, pwd)
    email=EmailMessage()
    email['From']=sender
    email['To']=receiver
    email['Subject']=subject
    email.set_content(body)
    server.send_message(email)
    server.close()
