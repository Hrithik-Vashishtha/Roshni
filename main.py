from chess_bot import ChessEngine
import chess

class Chess:
    def __init__(self, chess_engine):
        self.chess_engine = chess_engine

    def update(self):
        best_move = self.chess_engine.get_best_move()
        return self.chess_engine.update_position(best_move)

# Example usage:
chess_engine = ChessEngine()
chess_game = Chess(chess_engine)
chess_game.update()