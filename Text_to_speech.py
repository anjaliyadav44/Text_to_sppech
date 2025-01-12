from tkinter import *
from gtts import gTTS
from playsound import playsound
import os
from PIL import Image, ImageTk

root = Tk()
root.geometry("620x400")
root.configure(bg='ghost white')
root.title("TextTalker- TEXT TO SPEECH")

# Main Functions
def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text=Message)
    speech.save(f'{Message}.mp3')
    playsound(f'{Message}.mp3')
    os.remove(f'{Message}.mp3')

def Reset():
    Msg.set("")

def Exit():
    root.destroy()

panel = Frame(root)
panel.place(x=25, y=100)

# Load image using Pillow
try:
    img = Image.open('Text to Speech logo.png')
    img = ImageTk.PhotoImage(img)
    imgLbl = Label(panel, image=img)
    imgLbl.grid(rowspan=4, column=0)
except Exception as e:
    print("Error loading image:", e)

Label(root, text="TEXT TO SPEECH", font="arial 20 bold", bg='white smoke').pack()
Label(text="TextTalker", font='arial 15 bold', bg='white smoke', width='20').pack(side='bottom')

Msg = StringVar()
Label(root, text="Enter Text", font='arial 20 bold', bg='white smoke').place(x=400, y=100)

entry_field = Entry(root, textvariable=Msg, width='45')
entry_field.place(x=330, y=150)

Button(root, text="PLAY", font='arial 15 bold', width='5', bg='light Green', command=Text_to_speech).place(x=330, y=240)
Button(root, font='arial 15 bold', text='EXIT', width='5', bg='Red', command=Exit).place(x=420, y=240)
Button(root, font='arial 15 bold', text='RESET', width='6', command=Reset).place(x=510, y=240)

root.mainloop()
