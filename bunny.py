from datetime import datetime

import speech_recognition as sr
import speech_recognition as sr

import pyttsx3
import pywhatkit as pt
import datetime
import pyjokes
import wikipedia


# Mic Recognizer
listener = sr.Recognizer()


CONVERSATION_LOG = "CONVERSATION LOG.txt"
#text to speech starting
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 150)
#talk function

def talk(text):
    engine.say(text)
    engine.runAndWait()

#greeting function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if hour >= 1 and hour <=6:
        talk('its night time sir')
    elif hour >= 6 and hour <=12:
        talk('good morning sir')
    elif hour>=12 and hour <= 16:
        talk('good afternoon sir')
    else:
        talk('good evening sir')


def take_command():
    with sr.Microphone() as source:
        print('listening....')
        voice = listener.listen(source)
    try:

        print('recognizing')
        command = listener.recognize_google(voice,language= 'en-in')
        command = command.lower()
        print('converted')
        if 'alexa' in command:
            command = command.replace('alexa',' ')
            print('removed alexa')
        print(f'user said :{command}\n')
    except Exception as e:
        talk('how may help you')
        command = None
    return command

def run_bunny():
     command = take_command()


     print('searching operation')
     #if 'play song' in command:
            #song = command.replace('play', '')
            #talk('playing' + song)
           # print(song)
        #pt.playonyt(song)
        #joke
     if 'joke' in command:
            talk(pyjokes.get_joke())
            print(pyjokes.get_joke())

         #time
     elif 'time' in command:

            time = datetime.datetime.now().strftime("%I:%M %p") #%p for am or pm  H-24 hour   I-12 hour
            talk('its time now' + time)
            print('time is', time)

     elif 'who is' in command:
            talk('searching wikipedia')
            command = command.replace('who is ', " ")
            results = wikipedia.summary(command, sentences=2)
            print(results)
            talk(results)

     elif 'are you single' in command:
            talk('i am in relationship with wifi')
            print('done')

     elif 'developer' in command:
            talk('buneshwar and rushi ')

     elif 'stop' in command:
            talk('bye bye ')
            exit()

     else:
         talk('say it agian')
         command = take_command()


talk('lodu lalit')
wishMe()
while True:
     run_bunny()



