import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 120)
engine.say("The move is illegal, please try again, you have only, 3, chances left")
engine.runAndWait()