import pyaudio
import speech_recognition as sr
import wikipedia
import webbrowser
import urllib.request
import urllib.parse
import re
import datetime

r = sr.Recognizer()
def initSpeech():
    print("Listening")
    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)
    command = ""
    try:
        command = r.recognize_google(audio)
    except:
        print("Nothing")
    print(command)
    return command
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
    elif hour>=12 and hour<18:
        print("Good Afternoon!")
    else:
        print("Good Evening!")
if __name__ == "__main__":
    wishMe()
    while True:
        command = initSpeech().lower()
        if 'wikipedia' in command:
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2)
            print(results)
        elif 'open youtube' in command:
            webbrowser.open('youtube.com')
            query_string = urllib.parse.urlencode({"search_query": initSpeech().lower()})
            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
            webbrowser.open("http://www.youtube.com/watch?v=" + search_results[0])
        elif 'open amazon' in command:
            webbrowser.open('amazon.com')
        elif 'the time' in command:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strTime}")
        elif 'open google' in command:
            webbrowser.open('google.com')
        elif 'open facebook' in command:
            webbrowser.open('facebook.com')
        elif 'open v o l p' in command:
            webbrowser.open('classroom.volp.in')
        elif 'stop' in command:
            break