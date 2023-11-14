from speech_recognition_utils import audio_input
def uci_format():
    text = audio_input()
    text = text.lower()
    text = text.replace(" ", "")

    return text


# import spacy

# def convert_to_uci_with_nlp(spoken_move):
#     nlp = spacy.load("en_core_web_sm")
#     doc = nlp(spoken_move)

#     piece_mapping = {
#         "pawn": "",
#         "knight": "N",
#         "night": "N",
#         "bishop": "B",
#         "rook": "R",
#         "queen": "Q",
#         "king": "K"
#     }

#     uci_move = ""

#     for token in doc:
#         if token.text in piece_mapping:
#             uci_move += piece_mapping[token.text]
#         elif token.pos_ == "ADP" and token.text == "to":
#             pass  # Skip preposition "to"
#         elif token.pos_ == "NUM" and len(token.text) == 2:
#             uci_move += token.text.lower()  # Lowercase for board squares (e.g., "h3")

#     return uci_move if uci_move else None

# # Usage example
# spoken_move = "pawn to h3"
# uci_move_with_nlp = convert_to_uci_with_nlp(spoken_move.lower())  # Convert to lowercase for easier matching
# print("UCI move with NLP:", uci_move_with_nlp)
