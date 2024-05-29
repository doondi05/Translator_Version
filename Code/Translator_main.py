import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from gtts import gTTS
import os
import speech_recognition as sr

def translate_text():
    input_text = input_text_area.get("1.0", "end-1c")  
    target_language = target_language_var.get()  
    if input_text:
        translator = Translator()
        translated_text = translator.translate(input_text, dest=target_language).text
        output_text_area.delete("1.0", "end") 
        output_text_area.insert("1.0", translated_text)  
        text_to_speech(translated_text, target_language)  

def text_to_speech(text, lang):
    speak = gTTS(text=text, lang=lang, slow=False)
    speak.save("translated_voice.mp3")
    os.system("start translated_voice.mp3")

def capture_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        audio = recognizer.listen(source)
        try:
            voice_text = recognizer.recognize_google(audio)
            input_text_area.delete("1.0", "end")
            input_text_area.insert("1.0", voice_text)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))


root = tk.Tk()
root.title("Translation App")


inner_frame = tk.Frame(root)
inner_frame.pack(padx=10, pady=10)


input_text_label = tk.Label(inner_frame, text="Input Text:")
input_text_label.pack(anchor="w", padx=(0,5), pady=(0,5))
input_text_area = tk.Text(inner_frame, width=40, height=5)
input_text_area.pack(anchor="w", padx=(0,5))


languages = ['en', 'es', 'fr', 'de','te','ta','ja','ru','ml','hi']  
target_language_var = tk.StringVar()
target_language_label = tk.Label(inner_frame, text="Target Language:")
target_language_label.pack(anchor="w", padx=(0,5), pady=(5,5))
target_language_dropdown = ttk.Combobox(inner_frame, textvariable=target_language_var, values=languages, width=37)
target_language_dropdown.pack(anchor="w", padx=(0,5), pady=(0,5))
target_language_dropdown.current(0)  


submit_button = tk.Button(inner_frame, text="Translate", command=translate_text)
submit_button.pack(anchor="w", padx=(0,5), pady=(5,0))


voice_input_button = tk.Button(inner_frame, text="Voice Input", command=capture_voice)
voice_input_button.pack(anchor="w", padx=(0,5), pady=(5,0))


output_text_label = tk.Label(inner_frame, text="Translated Text:")
output_text_label.pack(anchor="w", padx=(0,5), pady=(10,5))
output_text_area = tk.Text(inner_frame, width=40, height=5)
output_text_area.pack(anchor="w", padx=(0,5))


root.mainloop()
