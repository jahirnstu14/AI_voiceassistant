import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os 
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning ")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon ")
    else:
        speak("Good Night")
    speak("I am Google Assistant. How may I help you?")
def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        query=r.recognize_google(audio, language="en-Us")#using google for voice recognition
        print(f"User said : {query}\n")#user will be printed 
    except Exception as e:
        #print(e)
        print("say that again please")#say that again will b printed in case of import 
        return "None"
    return query
def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.echo
    server.starttls()
    server.sendmail('mypassword@gmail.com', 'your password')
    server.login('mypassword@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
   
    while True:
        query=takeCommand().lower()#convert user voice into lower case text 
        #executing for logic tasks based on queary 
        if 'wikipedia'in query:
            speak('Searching Wikipeadia')
            query = query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir= 'D:\\audio song'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[random.randint(0,2)]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "jahirkhan.ice.nstu@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")    

   


