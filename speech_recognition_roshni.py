# # Speech Recognition:
# # Learn about speech recognition libraries or APIs in Python.
# # Familiarize yourself with how to capture and process audio input.

import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
recognizer = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable
with sr.Microphone() as source:
    print("Start Talking")
    audio_text = recognizer.listen(source)
    print("Time over, thank you")
    
    try:
        # using google speech recognition
        print("Text: "+recognizer.recognize_google(audio_text))
    except:
         print("Sorry, I did not get that")
