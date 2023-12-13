from flask import Flask, request, jsonify, render_template
from game import Chess
from chess_bot import ChessEngine
from db_handler import GameDatabase
from speech_recognition_utils import SpeechRecognition
from text_to_speech_utils import TextToSpeech


app = Flask(__name__)

game_database = GameDatabase()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play', methods=['GET'])
def play_game():
    speech_recognition = SpeechRecognition()
    text_to_speech = TextToSpeech()
    game_database = GameDatabase()
    chess_engine = ChessEngine()

    chess_game = Chess(chess_engine, speech_recognition, text_to_speech, game_database)
    text_to_speech.game_start()
    moves = chess_game.play_game()  
    
    # Store moves in the database
    return jsonify({"moves": moves})

@app.route('/get_moves/<int:id>', methods=['GET'])
def moves(id):
    moves_data = game_database.get_moves(id)

    if not isinstance(moves_data, str):
        moves = moves_data.get('moves')  
        if moves:  
            moves = [move[1] for move in moves]  
            return jsonify(moves), 200  

    return jsonify({'error': 'Moves not found'}), 404  


if __name__ == "__main__":
    app.run(debug=True)