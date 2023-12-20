import speech_recognition as sr

class SpeechRecognition:
    def audio_input(self):
        r = sr.Recognizer()
        r.dynamic_energy_threshold = False  # Disable dynamic energy threshold
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            print("Say Something")
            audio = r.listen(source)
            print("Time over, thank you")

            try:
                text = r.recognize_google(audio)
                # return text.lower().replace(" ", "")
                return text.lower()
            except sr.UnknownValueError:
                print("Sorry, I didn't get this")
                return None  # Return None when speech cannot be recognized



# class SpeechRecognition:
#     def audio_input(self):
#         r = sr.Recognizer()
#         with sr.Microphone() as source:
#             print("Say Something")
#             audio = r.listen(source)
#             print("Time over, thank you")
#             try:
#                 text = r.recognize_google(audio)
#                 return text.lower().replace(" ","")
#             except:
#                 print("Sorry, I didn't get this")
