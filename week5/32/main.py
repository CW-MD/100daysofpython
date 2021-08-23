from tkinter import Tk, Canvas, Label, Entry, Button, PhotoImage
import pandas
BACKGROUND_COLOR = "#B1DDC6"

#Pandas
#Key : Value
#French : 0 - 100
#English : 0 - 100
df = pandas.read_csv('data/french_words.csv')
translator = df.to_dict()

print(translator['French'][0])
print(translator['English'][0])
window = Tk()
#Images
CARD_FRONT = PhotoImage(file='images/card_front.png', width=800, height=600)
CARD_BACK = PhotoImage(file='images/card_back.png', width=400, height=250)
RIGHT_IMG =  PhotoImage(file='images/right.png' , width=100, height=100)
WRONG_IMG = PhotoImage(file='images/wrong.png', width=100, height=100)
#

window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title('Flash Cards')
canvas = Canvas(width=900, height=650)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0,row=0, columnspan=2)
canvas.create_image(450,350,image = CARD_FRONT)

canvas.create_text(450,150, text='Title', font=('Serif', 35, 'italic'))
canvas.create_text(450,275, text='Word', font=('Sans Serif', 50,))

yes_button = Button(image=RIGHT_IMG)
yes_button.grid(column=0,row=1)
no_button = Button(image=WRONG_IMG)
no_button.grid(column=1, row=1)













window.mainloop()