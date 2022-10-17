import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():

    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            order = listener.recognize_google(voice)
            #print(order)
            #if 'elon' in command:
               # command = command .replace('elon', '')
                #print(command)
    except:
        print(order)
        print('t5thet')
        pass
    return order


def run_alexa():
    talk('hi ahmed I''am Elon musk how can I help you ?')
    cmd = take_command()
    if 'play' in cmd:
        print(cmd)
        song = cmd.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in cmd:
        print(cmd)
        time = datetime.datetime.now()
        time = time.strftime('%H:%M:%S')
        print(time)
        talk('current time is ' + time)
    elif 'search for' in cmd:
        print(cmd)
        topic = cmd.replace('search for', '')
        talk('searching for' + topic)
        pywhatkit.info(topic, 5)
    else:
        print('I can not understand you')
        talk('I can not understand you')




run_alexa()
