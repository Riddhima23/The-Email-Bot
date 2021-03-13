import os
import json
import pyttsx3
import speech_recognition as sr
import smtplib
from email.message import EmailMessage
import threading
import queue
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import WORD
from tkinter import messagebox

def send():
    queue.put(e.get())
    e.delete(0,tk.END)

def speak(text):
    bot.say(text)
    bot.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        queue.put("Kurama:- Listening...\n")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        queue.put("Kurama:- Recognizing...\n")
        query = r.recognize_google(audio, language='en-in')
        print(f"You-->{query}\n")

    except Exception as e:
        queue.put("Kurama:- Sorry couldn\'t recognise that !\n")
        speak("Sorry couldn\'t recognise that !")
        query="\quit"

    return query

def send_email(sender,pwd,receiver, subject, body):
    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender,pwd)
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
