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
elist = {}
with open('data.json') as file:
    elist = json.load(file)
def get_email_info():
    talk('Hello! I am an email bot. I offer help to those who have hands but don\'t wanna use them! I would ask a few questions after which your email will be sent in a snap of fingers just like Thanos')
    talk('Please enter your email and password!')
    print('Email:')
    sender=input()
    print('Password:')
    pwd=input()
    talk('To whom you wanna send email? Type the name of the person!')
    print("Reciever's name:")
    name=input()
    print(elist)
    talk('Is the email address of the person already in the mail dictionary?')
    ans=get_info()
    print(receiver)
    talk('What is the subject of your email? ')
    subject=get_info()
    talk('What is the content of your email?')
    message=get_info()
    send_email(sender,pwd,receiver,subject,message)
    talk('Do you wanna send more emails or you wanna stop?')
    tell=get_info()
    if tell == 'yes':
        get_email_info()

get_email_info()
