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

    def illegal_move(self, move, count):
        self.engine.setProperty('rate', 120)
        self.engine.say(f"The move {move} is illegal, please try again, you have only, {count}, chances left")
        self.engine.runAndWait()

    def game_over(self):
        self.engine.setProperty('rate', 120)
        self.engine.say("Illegal Move, Game Over")
        self.engine.runAndWait()

    def checkmate_win(self):
        self.engine.setProperty('rate', 120)
        self.engine.say("Congratulations, you have checkmated your opponent")
        self.engine.runAndWait()

    def checkmate_lose(self):
        self.engine.setProperty('rate', 120)
        self.engine.say("you have been checkmated, game over!")
        self.engine.runAndWait()
