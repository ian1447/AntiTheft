import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
mic = sr.Microphone()

print("Start Talking!")

while True:
    with mic as source:
        audio = r.listen(source)
    words = r.recognize_google(audio)
    print(words)