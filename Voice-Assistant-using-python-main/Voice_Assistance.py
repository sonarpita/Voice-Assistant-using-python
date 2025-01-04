import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit
import os
import winshell
import pyjokes
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():

    speak("Good Evening !")
    assname = ("Jarvis 1 point o")
    speak("I am your Assistant")
    speak(assname)


def username():
    speak("What should i call you ?")
    uname = takeCommand()
    speak("Welcome")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome .  ", uname.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you ")
def get_news_forecast():
    # API endpoint for news forecast
    url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=ec7ff99f77174ce8a95d3581beb97e2e"

    # Make a GET request to the API
    response = requests.get(url)

    # Load the JSON response into a Python object
    data = json.loads(response.text)

    # Extract the top 3 news headlines and print them out
    for i in range(10):
        title = data["articles"][i]["title"]
        print(f"Headline {i+1}: {title}")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


if _name_ == '_main_':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()

    while True:

        query = takeCommand().lower()

        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
        if 'who is' in query:
            speak('Searching Wikipedia...')
            query = query.replace("who is", "")
            results = wikipedia.summary(query, 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'open brave' in query:
            speak("Here you go to Brave\n")
            webbrowser.open("brave.com")

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'open music' in query or "open song" in query:
            speak("Here you go with music")
            # music_dir = "G:\\Song"
            music_dir = "C:\\Users\\KIIT\\Music\\"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))

        elif 'news' in query:
            get_news_forecast()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Aditya.")

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())

        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif "why you came to world" in query:
            speak("Thanks to Aditya. further It's a secret")
        # TODO:
        elif 'power point presentation' in query:
            speak("opening Power Point presentation")
            power = r"C:\\Users\\KIIT\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
            os.startfile(power)

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Aditya")

        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister Aditya ")

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime('%I:%M %p')
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "update assistant" in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream=True)

            with open("Voice.py", "wb") as Pypdf:

                total_length = int(r.headers.get('content-length'))

                for ch in progress.bar(r.iter_content(chunk_size=2391975),
                                       expected_size=(total_length / 1024) + 1):
                    if ch:
                        Pypdf.write(ch)

        # NPPR9-FWDCX-D2C8J-H872K-2YT43
        elif "jarvis" in query:

            wishMe()
            speak("Jarvis 1 point o in your service Mister")
            speak(assname)


        elif "Good Morning" in query:
            speak("A warm" + query)
            speak("How are you Mister")
            speak(assname)

        elif "how are you" in query:
            speak("I'm fine, glad you me that")
            print("I'm fine, glad you me that")

        elif "i love kiit" in query:
            speak("I also love kiit")
            print("I also love kiit")
