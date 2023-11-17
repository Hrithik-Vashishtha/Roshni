import speech_recognition as sr
class SpeechRecognition:
    
    def audio_input(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say Something")
            audio = r.listen(source)
            print("Time over, thank you")
            try:
                text = r.recognize_google(audio)
                return text.lower().replace(" ","")
            except:
                print("Sorry, I didn't get this")
audio = SpeechRecognition()
print(audio.audio_input())