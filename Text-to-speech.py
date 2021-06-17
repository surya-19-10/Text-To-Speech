import os
from gtts import gTTS
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title('Text - To - Speech')
root.resizable(0,0)

f = Frame(root,bg = 'yellow')
f.pack(fill = BOTH)

f1 = Frame(root,bg = 'yellow')
f1.pack(fill = BOTH)

f2 = Frame(root,bg = 'yellow')
f2.pack(fill = BOTH)

label = Label(f,text = 'Text - To - Speech',font = 'elephant',bg = 'yellow',fg = 'red')
label.pack(padx = 10, pady = 10)

entry = Text(f1, width = 35, height = 5)
entry.pack(padx = 10, pady = 10)

def convert():
    text = entry.get(0.1,END)
    lan = 'en'
    filename = 'audio.mp3'

    def read():
        audio_created = gTTS(text = text, lang = lan)
        audio_created.save(filename)

        os.system(f'start {filename}')

    read()

btn = Button(f2, text = "CONVERT",font = 'georgia',relief = FLAT,bg = '#7133FF',command = convert)
btn.pack(padx = 10, pady = 10)

root.mainloop()
