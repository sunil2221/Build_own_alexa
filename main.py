import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                talk(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        talk('current time is ' + time)
    elif 'who is' in command:
        person = command.replace("who is", '')
        info = wikipedia.summary(person, 1)
        talk(info)
    elif 'what is' in command:
        question = command.replace("what is", '')
        info1 = wikipedia.summary(question, 1)
        talk(info1)
    elif 'date' in command:
        talk("sorry, I have a headache")
    elif 'are you single' in command:
        talk("I am in a relationship with wifi")
    elif 'joke' in command:
        talk(pyjokes.get_joke('en'))
    else:
        talk("please say the command again.")


while True:
    run_alexa()