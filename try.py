import speech_recognition as sr
r = sr.Recognizer()
while True:
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_sphinx(audio2)
            MyText = MyText.lower()
            print("Did you say " + MyText)

            if 'happy' in MyText:
                print("\N{slightly smiling face}")
                print('😁')
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occured")

