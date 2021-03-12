import smtp
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
