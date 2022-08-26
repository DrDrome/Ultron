import time

import PyPDF2
import pyttsx3
import datetime

import requests
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
#import cv2
import random
import instadownloader
import pyautogui
import instaloader
import PyPDF2


engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')

# print(voice[1].id)

engine.setProperty('voice', voice[1].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon!")
    elif hour >= 16 and hour < 21:
        speak("Good Evening!")
    else:
        speak("Hello!")
    speak("I am Ultron. How may I help you?!")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        r.energy_threshold = 200
        audio = r.listen(source#,timeout=1,phrase_time_limit=5)
                         )

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        speak("Say that again please...")
        return ""
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('drdrome29@gmail.com', 'your-pasword-here')
    server.sendmail('drdrome29@gmail.com', to, content)
    server.close()

def pdf_reader():
    book = open('C:\\amity\\Admission Letter.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"total number of pages in pdf is {pages}")
    speak("please enter the page number that you want me to read: ")
    pg = int(input(""))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)

if __name__ == "__main__":
    wish()
    #while True:
    if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'play music' in query:
            music_dir = 'C:\\Songs\\N'
            songs = os.listdir(music_dir)
            print(songs)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {strTime}")
            speak(f"The time is {strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\shyam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open command prompt' in query:
            #os.system("start cmd")
            codePath = "C:\\WINDOWS\\system32\\cmd.exe"
            os.startfile(codePath)

        #elif 'open camera' in query:
            #cap = cv2.VideoCapture(0)
            #while True:
                #ret, img = cap.read()
                #cv2.imshow('webcam',img)
                #k = cv2.waitkey(58)
                #if k==27:
                    #break
            #cap.release()
            #cv2.destroyAllWindows()


        elif 'send email' in query:
            try:
                speak("What should I write?")
                content = takeCommand()
                to = "drdrome29@gmail.com"
                sendEmail(to, content)
                speak("The Email has been sent!")
            except Exception as e:
                speak("Unable to send Email.!")

        elif "where am i" in query:
            speak("please wait, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                #print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                #print(geo_data)
                city = geo_data['city']
                #state = geo_Data['state']
                country = geo_data['country']
                speak(f"I am not sure, but I think we are in {city} city of {country} country")
            except Exception as e:
                speak("Sorry, due to network error I am not able to find where we are.")
                pass

        elif "instagram profile" in query:
            speak("please enter the username correctly")
            username = input("Enter username here: ")
            webbrowser.open(f"www.instagram.com/{username}")
            time.sleep(3)
            speak("would you like to download the profile picture of this account?")
            condition = takeCommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(username, profile_pic_only = True)
                speak("The profile pict ure has been saved in our main project folder.")
            else:
                pass

        elif "screenshot" in query:
            speak("Please tell me the name for this screenshot file")
            name = takeCommand().lower()
            speak("please hold the screen for a few seconds")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("the screenshot has been saved in our main project folder")

        elif "read pdf" in query:
            pdf_reader()

        elif "snake game" in query:
            codePath = "C:\\Users\\shyam\\PycharmProjects\\Ultron\\Snake Game.py"
            os.startfile(codePath)


        elif 'quit' in query:
            exit()
