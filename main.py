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


from speech_recognition_utils import audio_input
from chess_bot import ChessEngine

class ChessGame():
    def __int__(self):
        self.chess_engine = ChessEngine

    def player_move(self):
        print("player's Turn")
        return audio_input()

    def bot_move(self):
        print("bot move")
        return self.chess_engine.get_best_move()

    while True:
        pass