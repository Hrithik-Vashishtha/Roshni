# import pyttsx3

# class TextToSpeech:
#     def __init__(self, engine):
#         self.engine = pyttsx3.init()          

#     def speech(move):
#         engine.setProperty('rate', 120)
#         voices = engine.getProperty('voices')   
#         engine.setProperty('voice', voices[1].id) 
#         engine.say("moved played by opponent is", move)
#         return engine.runAndWait()
# text = TextToSpeech()
# text.speech('e1e2')

import pyttsx3

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 120)  # Set speech rate here

    def speech(self, move):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)  # Set voice here
        self.engine.say("The move played by the opponent is " + move)
        self.engine.runAndWait()
