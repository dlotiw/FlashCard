from tkinter import *
from tkinter import messagebox
import pandas
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
words_to_learn = []
#----------Creating FlashCard----#

class Card:
    def __init__(self, language) -> None:
        self.front = PhotoImage(file="FlashCard/images/card_front.png")
        self.back = PhotoImage(file="FlashCard/images/card_back.png")
        self.image = self.front
        self.language = language
        self.word_spanish = ""
        self.word_english = ""
        self.get_word()
        

    def flip_card(self):
        if self.image == self.front:
            self.image = self.back
            self.language = "English"
        else:
            self.image = self.front
            self.language = "Spanish"
    
    def get_word(self):
        global words_to_learn
        try:
            data = pandas.read_csv("FlashCard/data/words_to_learn.csv")
            words_to_learn = data.to_dict(orient='records')
        except pandas.errors.EmptyDataError:
            data = pandas.read_csv("FlashCard/data/spanish_words_200.csv")
        except FileNotFoundError:
            data = pandas.read_csv("FlashCard/data/spanish_words_200.csv")
        words = data.to_dict(orient="records")
        text=random.choice(words)
        self.word_spanish = text['Spanish']
        self.word_english = text['English']

    
def change():
    cardo.flip_card()
    canvas.itemconfig(canvas_image,image=cardo.image)
    canvas.itemconfig(word,text=cardo.word_english,fill="white")
    canvas.itemconfig(language,text=cardo.language,fill="white")

def new_card():
    global cardo
    cardo = Card("Spanish")
    canvas.itemconfig(canvas_image,image=cardo.image)
    canvas.itemconfig(language,text=cardo.language,fill='black')
    canvas.itemconfig(word,text=cardo.word_spanish,fill='black')
        
#----------Buttons Click-------#
def righ_button_click():
    global cardo
    try:
        words_to_learn.remove({"Spanish": cardo.word_spanish,"English": cardo.word_english})
    except ValueError:
        pass
    try:
        df = pandas.DataFrame(words_to_learn)
        df.to_csv("FlashCard/data/words_to_learn.csv",index=False)
    except pandas.errors.EmptyDataError:
        pass
    new_card()
    screen.after(3000,change)

def wrong_button_click():
    global cardo
    if cardo.word_spanish not in words_to_learn:
        words_to_learn.append({"Spanish": cardo.word_spanish,"English": cardo.word_english})
    new_card()
    screen.after(3000,change)

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
            df = pandas.DataFrame(words_to_learn)
            df.to_csv("FlashCard/data/words_to_learn.csv",index=False)
            screen.destroy()

#---------------UI--------------#

#Main window
screen = Tk()
screen.title("FlashCards")
screen.config(padx=50,pady=50,background=BACKGROUND_COLOR)
cardo = Card("Spanish")

#FlashCard
canvas = Canvas(width=800,height=526,background=BACKGROUND_COLOR,highlightthickness=0)
canvas_image = canvas.create_image(400,263,image=cardo.front)
language = canvas.create_text(400,150,text=cardo.language,font=("Ariel",40,"italic"))
word = canvas.create_text(400,263,text=cardo.word_spanish,font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)


#Wrong button
wrong_image = PhotoImage(file="FlashCard/images/failed.png")
wrong_button = Button(image=wrong_image,background=BACKGROUND_COLOR,highlightthickness=0,activebackground=BACKGROUND_COLOR,bd=0,command=wrong_button_click)
wrong_button.grid(row=1,column=0)

#Right button
right_image = PhotoImage(file="FlashCard/images/correct.png")
right_button = Button(image=right_image,background=BACKGROUND_COLOR,highlightthickness=0,activebackground=BACKGROUND_COLOR,bd=0,command=righ_button_click)
right_button.grid(row=1,column=1)

screen.after(3000,change)

screen.protocol("WM_DELETE_WINDOW", on_closing)
screen.mainloop()

