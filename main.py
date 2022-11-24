import speech_recognition as sr
from google_trans_new import google_translator
from gtts import gTTS
from playsound import playsound
import os


r = sr.Recognizer()
translator = google_translator()
mic = sr.Microphone()

while True:
    with mic as source:
        print('Speak now!')
        audio = r.listen(source)

        try:
            speech_text = r.recognize_google(audio)
            print(speech_text)
            if speech_text in ('exit', 'close', 'stop'):
                break
        except sr.UnknownValueError:
            print('could not understand')
        except sr.RequestError:
            print('Could not request result from google')

        new_lang = translator.translate(speech_text, lang_tgt='zh-tw')
        print(new_lang)

        voice = gTTS(new_lang, lang='zh-tw')
        voice.save('voice.mp3')
        playsound('voice.mp3')
        os.remove('voice.mp3')
