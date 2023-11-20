from stockfish import Stockfish
import chess
class ChessEngine():
    def __init__(self):
        # Initialize the Stockfish engine
        self.stockfish = Stockfish("C:/ProgramData/stockfish/stockfish-windows-x86-64-modern.exe")
        self.stockfish.set_fen_position("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
        self.board = chess.Board()

    def set_position(self, fen):
        self.stockfish.set_fen_position(fen)

    def get_best_move(self):
        return self.stockfish.get_best_move()

    def get_eval_bar(self):
        return self.stockfish.get_evaluation()

    def legal_move(self, move): 
        return self.stockfish.is_move_correct(move)

    def reset_board(self):
        self.stockfish.set_fen_position(chess.STARTING_FEN)

    def update_position(self, move):
        self.stockfish.make_moves_from_current_position(move)

    def get_current_position(self):
        return self.stockfish.get_fen_position()

    def set_elo_rating(self, data):
        self.stockfish.set_elo_rating(data)

    def is_checkmate(self):
        return self.board.is_checkmate()
    
    def get_board(self):
        return self.stockfish.get_board_visual()
    
