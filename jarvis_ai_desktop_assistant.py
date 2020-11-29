import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")

    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    '''
        it takes microphone input from user and give string output 
    '''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listing...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n" )
    except Exception as e:
        print(e)

        print("Say that again...")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('hjpadaliya@gmail.com', 'H!4en@h!y@')
    server.sendmail('secure.hiren@gmail.com', to, content)
    server.close()
if __name__ == "__main__":
    # speak('Hiren is good Boy')
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for Executing tasks based on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            chrome_browser = webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe  %s')
            chrome_browser.open('youtube.com')

        elif 'open google' in query:
            chrome_browser = webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe  %s')
            chrome_browser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir = 'F:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"Sir, The time is {strtime}")

        elif 'open code' in query:
            code_path = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif 'email to hiren' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "secure.hiren@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak('Sorry! I am not able to send email')
