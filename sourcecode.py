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


# sending
def send():
    queue.put(e.get())
    e.delete(0, tk.END)


# speaking
def speak(text):
    bot.say(text)
    bot.runAndWait()


# taking input speech command
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        queue.put("Kurama:- Listening...\n\n")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        queue.put("Kurama:- Recognizing...\n\n")
        query = r.recognize_google(audio, language='en-in')
        print(f"You-->{query}\n")

    except Exception as e:
        queue.put("Kurama:- Sorry couldn\'t recognise that !\n\n")
        speak("Sorry couldn\'t recognise that !")
        query = "\quit"

    return query


# sending email
def send_email(sender, pwd, receiver, subject, body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, pwd)
    email = EmailMessage()
    email['From'] = sender
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(body)
    server.send_message(email)
    server.close()


# data.json(dictionary to json and vice a versa)
elist = {}
with open('data.json') as file:
    elist = json.load(file)


# main loop
def my_loop(queue):
    queue.put(
        "Hey Pal! This is Kurama , your personal Mail Assistant, in short  the Email Bot! I will help you in sending emails with minimum effort !\n \n")
    speak(
        "Hey Pal! This is Kurama , your personal Mail Assistant, in short  the Email Bot! I will help you in sending emails with minimum effort ! ")
    while True:
        queue.put("Kurama:- Please enter your email and password:\n")
        speak("Please enter your email: and password:")
        email = queue.get()
        password = queue.get()
        queue.put("Kurama:- To whom do you want to send the mail?\n\n")
        speak("To whom do you want to send the mail?")
        reply = queue.get()
        queue.put("Kurama:- Is the email address of the person you want to send email to present in our mail list ?\n\n")
        speak("Is the email address of the person you want to send email to present in our mail list ?")
        queue.put("Email List:\n\n")
        queue.put(elist)
        queue.put("\n\n")
        ans = takecommand().lower()
        if ans == "\quit":
            queue.put("\quit")
            break
        elif ans == "no":
            queue.put("Kurama:- Enter the email of the recipient:\n\n")
            speak("Enter the email of the recipient:")
            name = queue.get()
            elist[reply] = name
            t = len(elist)
            with open('data.json', 'a') as outfile:
                json.dump(elist, outfile, indent=4)
        queue.put("Kurama:- What will be the subject of the mail ?\n\n")
        speak("What will be the subject of the mail?")
        sub = takecommand().lower()
        if sub == "\quit":
            queue.put("\quit")
            break
        queue.put("You:- " + sub + "\n\n")
        queue.put("Kurama:- What will be the content of your mail ?\n\n")
        speak("What will be the content of your mail?")
        content = takecommand().lower()
        if content == "\quit":
            queue.put("\quit")
            break
        queue.put("You:- " + content + "\n\n")
        send_email(email, password, elist[reply], sub, content)
        queue.put(
            "Kurama:- Congratulations! You were able to send your first mail! Do you want to send more emails or you want to stop?\n\n")
        speak(
            "Congratulations ! You were able to send your first mail ! Do you want to send more emails or you want to stop ? ")
        ans = takecommand().lower()
        if ans == "\quit":
            queue.put("\quit")
            break
        elif ans == "stop":
            queue.put("Kurama-: Sayonara from Kurama ! I hope to see you again ! Till then have a good day! \n\n")
            speak("Sayonara from Kurama ! I hope to see you again ! Till then have a good day ! ")
            queue.put("\quit")
            break


def update_text():
    if not queue.empty():
        text = queue.get()
        if text == '\quit':
            root.destroy()
            return
        else:
            t.insert('end', text)

    root.after(200, update_text)


# driving function
if __name__ == "__main__":
    bot = pyttsx3.init('sapi5')
    bot.setProperty("rate", 155)
    voices = bot.getProperty('voices')
    bot.setProperty('voice', voices[0].id)
    root = tk.Tk()
    t = tk.Text(root, height=20, width=100, wrap=WORD)
    font_tuple = ("Teletype", 15)
    e = tk.Entry(root, width=80, fg="white", font=font_tuple, bg="#293552")
    e.grid(row=1, column=0)
    t.config(background="#07122b", font=font_tuple, fg="white")
    send = tk.Button(root, text="Send", command=send, bg="blue violet", font=font_tuple, fg="floral white",
                     activebackground="darkgreen", activeforeground="lightcyan").grid(row=1, column=1)
    t.grid(row=0, column=0, columnspan=2)
    root.title("KURAMA")
    queue = queue.Queue()

    update_text()

    task = threading.Thread(target=my_loop, args=(queue,))
    task.start()

    root.mainloop()

    task.join()
