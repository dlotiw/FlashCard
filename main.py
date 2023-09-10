from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"

#---------------UI--------------#

#Main window
screen = Tk()
screen.title("FlashCards")
screen.config(padx=50,pady=50,background=BACKGROUND_COLOR)

#FlashCard
canvas = Canvas(width=800,height=526,background=BACKGROUND_COLOR,highlightthickness=0)
card = PhotoImage(file="FlashCard/images/card_front.png")
canvas.create_image(400,263,image=card)
language = canvas.create_text(400,150,text="Spanish",font=("Ariel",40,"italic"))
word = canvas.create_text(400,263,text="tekst",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

#Wrong button
wrong_image = PhotoImage(file="FlashCard/images/failed.png")
wrong_button = Button(image=wrong_image,background=BACKGROUND_COLOR,highlightthickness=0)
wrong_button.grid(row=1,column=0)

#Right button
right_image = PhotoImage(file="FlashCard/images/correct.png")
right_button = Button(image=right_image,background=BACKGROUND_COLOR,highlightthickness=0,)
right_button.grid(row=1,column=1)





screen.mainloop()