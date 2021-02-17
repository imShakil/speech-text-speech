import pyttsx3
import speech_recognition


sr = speech_recognition.Recognizer()
engine = pyttsx3.init()


def speak_text(command_line):

    #  engine.setProperty('voice', voices[1].id)
    engine.say(command_line)
    engine.runAndWait()


def record_voice():
    while True:
        try:
            with speech_recognition.Microphone() as source:
                sr.adjust_for_ambient_noise(source, duration=0.2)
                audio = sr.listen(source)
                text = sr.recognize_google(audio, show_all=True)
                text = text.lower()

                print("Did you say "+text)
                speak_text(text)
        except speech_recognition.RequestError as e:
            print(e)
        except speech_recognition.UnknownValueError as e:
            print(e)


def listen_audio():
    audio = speech_recognition.AudioFile('en-US_Broadband_sample1.wav')
    with audio as source:
        a = sr.record(source)
        text = sr.recognize_google(a)
        print(text)
        speak_text(text)


if __name__ == '__main__':
    listen_audio()
