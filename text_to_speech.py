from chess_bot import ChessEngine
import chess
import chess.svg

# Create an instance of ChessEngine
chess_engine = ChessEngine()

# Update the position with a move
# move = 
chess_engine.update_position(['e2e3'])

# Get the current position
current_position = chess_engine.get_current_position()

# Create a chess.Board from the FEN representation
board = chess.Board(fen=current_position)

print(board)