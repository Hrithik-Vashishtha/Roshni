import chess
from stockfish import Stockfish

class Stockfish():
    def engine(self):
    # Initialize the Stockfish engine
    stockfish = Stockfish("C:/ProgramData/stockfish/stockfish-windows-x86-64-modern.exe")
    print(stockfish)