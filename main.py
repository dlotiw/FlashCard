from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

#----------Creating FlashCard----#

def add_flash_card(type):
    try:
        data = pandas.read_csv("FlashCard/data/spanish_words_200.csv")
    except FileNotFoundError:
        messagebox.askretrycancel("No words to learn file found","Not found words list, make sure there is espanol_words.csv file in data folder and try again")
    words = data.to_dict(orient="records")
    canvas_text=random.choice(words)
    if type == 'es':
        canvas.itemconfig(word,text=canvas_text['Spanish'])
    elif type == 'en':
        canvas.itemconfig(word,text=canvas_text['English'])
        
#----------Buttons Click-------#
def right_button_click():
    add_flash_card('es')
    flip_card(0)


def wrong_button_click():
    add_flash_card('en')
    flip_card(1)

def flip_card(side):
    if side == 1:
        canvas.itemconfig(canvas_image,image=card_back)
        canvas.itemconfig(language,text='English',fill='white')
        canvas.itemconfig(word,fill='white')
    if side == 0:
        canvas.itemconfig(canvas_image,image=card_front)
        canvas.itemconfig(language,text ='Spanish',fill='black')
        canvas.itemconfig(word,fill='black')
#---------------UI--------------#

#Main window
screen = Tk()
screen.title("FlashCards")
screen.config(padx=50,pady=50,background=BACKGROUND_COLOR)

#FlashCard
canvas = Canvas(width=800,height=526,background=BACKGROUND_COLOR,highlightthickness=0)
card_front = PhotoImage(file="FlashCard/images/card_front.png")
card_back = PhotoImage(file="FlashCard/images/card_back.png")
canvas_image = canvas.create_image(400,263,image=card_front)
language = canvas.create_text(400,150,text="Spanish",font=("Ariel",40,"italic"))
word = canvas.create_text(400,263,text="tekst",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)


#Wrong button
wrong_image = PhotoImage(file="FlashCard/images/failed.png")
wrong_button = Button(image=wrong_image,background=BACKGROUND_COLOR,highlightthickness=0,activebackground=BACKGROUND_COLOR,bd=0,command=wrong_button_click)
wrong_button.grid(row=1,column=0)

#Right button
right_image = PhotoImage(file="FlashCard/images/correct.png")
right_button = Button(image=right_image,background=BACKGROUND_COLOR,highlightthickness=0,activebackground=BACKGROUND_COLOR,bd=0,command=right_button_click)
right_button.grid(row=1,column=1)



screen.mainloop()