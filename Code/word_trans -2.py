import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os
recog1 = spr.Recognizer()
mc = spr.Microphone()
while True:
    with mc as source:
        print("Speak something or say 'exit' to end:")
        recog1.adjust_for_ambient_noise(source, duration=0.2)
        audio = recog1.listen(source)

    try:
        MyText = recog1.recognize_google(audio)
        MyText = MyText.lower()
        print("You said:", MyText)
        if 'exit' in MyText:
            print("Exiting...")
            break
        translator = Translator()
        from_lang = 'en'
        to_lang = 'te'
        translated_text = translator.translate(MyText, src=from_lang, dest=to_lang).text
        speak = gTTS(text=translated_text, lang=to_lang, slow=False)
        speak.save("captured_voice.mp3")
        os.system("start captured_voice.mp3")

    except spr.UnknownValueError:
        print("Unable to Understand the Input")

    except spr.RequestError as e:
        print("Unable to provide Required Output: ", e)
