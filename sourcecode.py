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
