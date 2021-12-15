from tkinter import *
import pywhatkit
import tkinter
import requests
from PIL import Image, ImageTk


def listen_music():
    music = music_text.get()
    pywhatkit.playonyt(music)


app = Tk()
app.title("Youtube Music")
app.geometry("500x250")

bg = ImageTk.PhotoImage(file="back.jpg")
canvas = Canvas(app, width=700, height=350)
canvas.pack(fill=BOTH, expand=True)
canvas.create_image(0, 0, image=bg, anchor="nw")

music_text = StringVar()
music_entry = Entry(app, textvariable=music_text)
music_entry.place(x=200, y=50)
search_button = Button(app, text="Search", width=12, command=listen_music)
search_button.place(x=220, y=80)
app.mainloop()
