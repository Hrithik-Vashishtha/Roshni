import chess
from stockfish import Stockfish
class ChessEngine():
    def __init__(self):
        # Initialize the Stockfish engine
        self.stockfish = Stockfish("C:/ProgramData/stockfish/stockfish-windows-x86-64-modern.exe")

    def set_position(self, fen):
        self.stockfish.set_fen_position(fen)

    def get_best_move(self):
        self.stockfish.get_best_move()

    def get_eval_bar(self):
        self.stockfish.get_evaluation()




