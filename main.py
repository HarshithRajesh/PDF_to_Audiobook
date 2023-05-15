import os
from tkinter import *
from flask import Flask
from PyPDF2 import PdfReader
import pyttsx3
from tkinter import filedialog
import keyboard



windows = Tk()
windows.title("PDF to Audio")
windows.config(pady=50,padx=50,bg='#E06469')


def pdfReader():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select image",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("All file","*.*")))
    engine = pyttsx3.init()
    reader = PdfReader(filename)
    page = reader.pages[0]
    text = page.extract_text()
    engine.say(text)
    engine.runAndWait()


canvas = Canvas(width=250,height=250,bg="#E06469",highlightthickness=0)
canvas.grid(row=1,column=1)
title_label = Label(text = "PDF TO AUDIO",fg='#AFD3E2',bg='#E06469',font=("Ariel",26,"bold"))
title_label.grid(column=1,row=1)
btn = Button(text="Select File",command=pdfReader)
btn.grid(row=2,column=1)

windows.mainloop()
