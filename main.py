# from chess_bot import ChessEngine
# import chess

# class Chess:
#     def __init__(self, chess_engine):
#         self.chess_engine = chess_engine

#     def move_input(self):
#         input = audio_input()
#         return input

#     def update(self):
#         best_move = self.chess_engine.get_best_move()

#         if best_move and self.chess_engine.legal_move(best_move):
#             return self.chess_engine.update_position([best_move])
#         else:
#             print("Invalid move or no legal moves.")
#             return False


# # Example usage:
# chess_engine = ChessEngine()
# chess_game = Chess(chess_engine)
# chess_game.update()


# from speech_recognition_utils import audio_input
# from chess_bot import ChessEngine

# class ChessGame():
#     def __int__(self):
#         self.chess_engine = ChessEngine

#     def player_move(self):
#         print("player's Turn")
#         audio = audio_input()

#     def bot_move(self):
#         print("bot move")
#         return self.chess_engine.get_best_move()

#     def play_game(self):
#         while True:
#             #players turn
#             player_move_str  = self.player_move()
#             if player_move_str:
#                 if self.chess_engine.legal_move(player_move_str):
#                     self.chess_engine.update_position(player_move_str)
#             else:
#                 print("No input recieved, try again")
#                 return self.play_game
            
#             #bot's turn
#             bot_move_str = self.bot_move
#             return self.chess_engine.update_position(bot_move_str)

#             current_position = self.chess_engine.get_current_position()
#             print("current_position: ", current_position)
# chess = ChessGame()
# chess.play_game()

from chess_bot import ChessEngine
from speech_recognition_utils import SpeechRecognition
from chess import Board

class Chess:
    def __init__(self, chess_engine, speech_recognition):
        self.chess_engine = chess_engine
        self.speech_recognition = speech_recognition
    
    def player_move(self):
        audio_input = self.speech_recognition.audio_input()
        if audio_input and self.chess_engine.legal_move(audio_input):
            print(audio_input)
            return self.chess_engine.update_position([audio_input])
        return "Try Again"

    def bot_move(self):
        bot_input = self.chess_engine.get_best_move()
        return self.chess_engine.update_position([bot_input])


chess_engine = ChessEngine()
speech_recognition = SpeechRecognition()
chess_game = Chess(chess_engine, speech_recognition)
chess_game.player_move()
chess_game.bot_move()
