from chess_bot import ChessEngine
from speech_recognition_utils import SpeechRecognition
from chess import Board
from text_to_speech_utils import TextToSpeech
from db_handler import GameDatabase

class Chess:
    def __init__(self, chess_engine, speech_recognition, text_to_speech, game_database):
        self.chess_engine = chess_engine
        self.speech_recognition = speech_recognition
        self.text_to_speech = text_to_speech
        self.game_database = game_database
        self.count = 3
        self.moves_list = []
        # self.time = time
    
    def player_move(self):
        while self.count > 0:
            audio_input = self.speech_recognition.audio_input()
            if audio_input and self.chess_engine.legal_move(audio_input):
                print(audio_input)
                self.chess_engine.update_position([audio_input])
                self.moves_list.append(audio_input)
                print(self.chess_engine.get_board())
                if self.chess_engine.is_checkmate():
                    self.text_to_speech.checkmate_win()
                    return True
                return False
            else:
                self.count -= 1
                if self.count == 0:
                    self.text_to_speech.game_over()
                    return True
                self.text_to_speech.illegal_move(audio_input, self.count)
        return False


    def bot_move(self):
        bot_input = self.chess_engine.get_best_move()
        self.chess_engine.update_position([bot_input])
        print(f"opponent move is {bot_input}")
        self.moves_list.append(bot_input)
        print(self.chess_engine.get_board())
        self.text_to_speech.speech(bot_input)
        if self.chess_engine.is_checkmate():
            self.text_to_speech.checkmate_lose()
            return True

    def play_game(self):
        while True: 
            if self.player_move():
                break
            if self.bot_move():
                break
        # Concatenate all moves into a single string
        moves_string = ' '.join(self.moves_list)

        # Store all moves as a single entry in the database
        self.game_database.create_game(moves_string)
        return moves_string 


# chess_engine = ChessEngine()
# speech_recognition = SpeechRecognition()
# text_to_speech = TextToSpeech()
# game_database = GameDatabase()

# chess_game = Chess(chess_engine, speech_recognition, text_to_speech, game_database)
# text_to_speech.game_start()
# moves_list = chess_game.play_game()