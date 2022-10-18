import pyttsx3


def SpeakText(command):

    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

SpeakText("Good morning, Sunil")