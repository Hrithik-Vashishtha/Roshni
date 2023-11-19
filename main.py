# from chess_bot import ChessEngine
# import chess

# class Chess:
#     def __init__(self, stockfish):
#         self.stockfish = stockfish

#     def move_input(self):
#         input = audio_input()
#         return input

#     def update(self):
#         best_move = self.stockfish.get_best_move()

#         if best_move and self.stockfish.legal_move(best_move):
#             return self.stockfish.update_position([best_move])
#         else:
#             print("Invalid move or no legal moves.")
#             return False


# # Example usage:
# stockfish = ChessEngine()
# chess_game = Chess(stockfish)
# chess_game.update()


# from speech_recognition_utils import audio_input
# from chess_bot import ChessEngine

# class ChessGame():
#     def __int__(self):
#         self.stockfish = ChessEngine

#     def player_move(self):
#         print("player's Turn")
#         audio = audio_input()

#     def bot_move(self):
#         print("bot move")
#         return self.stockfish.get_best_move()

#     def play_game(self):
#         while True:
#             #players turn
#             player_move_str  = self.player_move()
#             if player_move_str:
#                 if self.stockfish.legal_move(player_move_str):
#                     self.stockfish.update_position(player_move_str)
#             else:
#                 print("No input recieved, try again")
#                 return self.play_game
            
#             #bot's turn
#             bot_move_str = self.bot_move
#             return self.stockfish.update_position(bot_move_str)

#             current_position = self.stockfish.get_current_position()
#             print("current_position: ", current_position)
# chess = ChessGame()
# chess.play_game()

from chess_bot import ChessEngine
from speech_recognition_utils import SpeechRecognition
from chess import Board
from text_to_speech_utils import TextToSpeech

class Chess:
    def __init__(self, chess_engine, speech_recognition, text_to_speech):
        self.chess_engine = chess_engine
        self.speech_recognition = speech_recognition
        self.text_to_speech = text_to_speech
        self.count = 3
    
    def player_move(self):
        audio_input = self.speech_recognition.audio_input()
        if audio_input and self.chess_engine.legal_move(audio_input):
            print(audio_input)
            self.chess_engine.update_position([audio_input])
            print(self.chess_engine.get_board())
        else:
            self.count -= 1
            if self.count == 0:
                self.text_to_speech.game_over()
            self.text_to_speech.illegal_move(audio_input, self.count)
            self.player_move()

    def bot_move(self):
        bot_input = self.chess_engine.get_best_move()
        self.chess_engine.update_position([bot_input])
        self.text_to_speech.speech(bot_input)
        print(self.chess_engine.get_board())

    def play_game(self):
        while True:
            


chess_engine = ChessEngine()
speech_recognition = SpeechRecognition()
text_to_speech = TextToSpeech()
chess_game = Chess(chess_engine, speech_recognition, text_to_speech)
chess_game.player_move()
chess_game.bot_move()
