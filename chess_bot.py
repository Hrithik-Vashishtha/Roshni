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

    def legal_move(self, move):
        self.stockfish.is_move_correct(move)

    def reset_board(self):
        self.stockfish.set_fen_position(chess.STARTING_FEN)

    def update_position(self, move):
        self.stockfish.make_moves_from_current_position(move)

    def get_current_position(self):
        self.stockfish.get_fen_position()

    def set_elo_rating(self, data):
        self.stockfish.set_elo_rating(data)







