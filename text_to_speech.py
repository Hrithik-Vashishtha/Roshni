import pyttsx3
engine = pyttsx3.init()          
engine.setProperty('rate', 120)
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id) 
engine.say("moved played by opponent is e1e2")
engine.runAndWait()
