# import pyttsx3
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
# engine.setProperty('rate', 120)
# engine.say("The move is illegal, please try again, you have only, 3, chances left")
# engine.runAndWait()

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
print("Hello")