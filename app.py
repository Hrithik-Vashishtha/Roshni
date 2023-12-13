from flask import Flask, request, jsonify
from game import Chess
from chess_bot import ChessEngine
from db_handler import GameDatabase
from speech_recognition_utils import SpeechRecognition
from text_to_speech_utils import TextToSpeech

app = Flask(__name__)
@app.route('/play', methods=['GET'])
def play_game():
    chess_engine = ChessEngine()
    speech_recognition = SpeechRecognition()
    text_to_speech = TextToSpeech()
    game_database = GameDatabase()

    chess_game = Chess(chess_engine, speech_recognition, text_to_speech, game_database)
    text_to_speech.game_start()
    moves = chess_game.play_game()  # Start playing the game
    
    # Store moves in the database
    return jsonify({"moves": moves})


if __name__ == "__main__":
    app.run(debug=True)