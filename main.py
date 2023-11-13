from chess_bot import ChessEngine
import chess

chess_engine = ChessEngine()

initial_position = chess.STARTING_FEN   
chess_engine.set_position(initial_position)

best_move = chess_engine.get_best_move()

print(f"The best move is: {best_move}")

def best_move():
    pass