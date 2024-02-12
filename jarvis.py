import pyttsx3 #text to speech converter
import datetime #helps in identifying date and time
import speech_recognition as sr #helps in taking audio from microphone
import wikipedia
import webbrowser
import os
import random 
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe(name):
    hour=int(datetime.datetime.now().hour)
    if( hour>=0 and hour<12):
        speak(f"Good morning {name}")
    elif hour>=12 and hour<18:
        speak(f"good afternoon {name}")
    else:
        speak(f"good evening {name}")
    speak("How can I Help you at this moment?")
    
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return None
    return query
def sendemail(to,content):
    server=smtplib.SMTP('smtp@gmail.com',465)
    server.ehlo()
    server.starttls()
    server.login('syemeed@gmail.com','*********')#password was hidden due to privacy issues
    server.sendmail('syemeed@gmail.com',to,content)
    server.close()

if __name__=="__main__":
    speak("I am JARVIS Sir!May i know who is accessing system right now? ")
    name=takeCommand()
    wishMe(name)
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
        elif 'play music' in query:
            music_dir='D:\MUSIC'
            random_number=random.randint(0,6)
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random_number]))
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir,the time is{strtime}")
        elif 'thank you' in query:
            speak("You are always welcome sir!")
        elif 'open code' in query:
            codepath="C:\\Users\\syeme\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'open whatsapp' in query:
            codepath="C:\\Users\\syeme\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'open capcut' in query:
            editpath="C:\\Users\\syeme\\AppData\\Local\\CapCut\\Apps\\CapCut.exe --src3"
            os.startfile(editpath)
        elif 'send email' in query:
            try:
                speak("What should i say")
                content=takeCommand()
                to="bagundalitfi@gmail.com"
                sendemail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry sir,I cant send mails at these moment")
        
