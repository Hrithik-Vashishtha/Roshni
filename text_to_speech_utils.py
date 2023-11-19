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
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)  # Set speech rate here

    def speech(self, move):
        self.engine.setProperty('rate', 120)
        self.engine.say(f"The move played by the opponent is")
        self.engine.runAndWait()
        
        # Second line spoken at rate 100
        self.engine.setProperty('rate', 80)
        self.engine.say(move)
        self.engine.runAndWait()

        self.engine.setProperty('rate', 120)
        self.engine.say("Please play your move")
        self.engine.runAndWait()