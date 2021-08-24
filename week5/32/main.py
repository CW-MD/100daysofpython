from tkinter import Tk, Canvas, Label, Entry, Button, PhotoImage
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
#Key words declared to make indexing df easier
FR= 'French'
EN = 'English'




#Pandas
#Key : Value
#French : 0 - 100
#English : 0 - 100
df = pandas.read_csv('data/french_words.csv')
translator = df.to_dict(orient='records')
current_card = {}
print(translator[0][FR], translator[0][EN])


def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    
    
    # if answer == True and current_card:
    #     translator.remove(current_card)
   
    current_card = random.choice(translator)
    canvas.itemconfig(card, image=CARD_FRONT)
    canvas.itemconfig(card_title, text='French')
    canvas.itemconfig(card_word, text=current_card[FR])
    flip_timer = window.after(3000,flip)
    


def flip():
    canvas.itemconfig(card, image=CARD_BACK)
    canvas.itemconfig(card_title, text='English')
    canvas.itemconfig(card_word, text=current_card[EN])



window = Tk()
#Images
CARD_FRONT = PhotoImage(file='images/card_front.png', width=800, height=600)
CARD_BACK = PhotoImage(file='images/card_back.png', width=800, height=600)
RIGHT_IMG =  PhotoImage(file='images/right.png' , width=100, height=100)
WRONG_IMG = PhotoImage(file='images/wrong.png', width=100, height=100)
#

flip_timer = window.after(3000, flip)

window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title('Flash Cards')
canvas = Canvas(width=900, height=650)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0,row=0, columnspan=2)
card = canvas.create_image(450,350,image = CARD_FRONT)

card_title = canvas.create_text(450,150, text='Title', font=('Serif', 35, 'italic'))
card_word = canvas.create_text(450,275, text='Word', font=('Sans Serif', 50,))

yes_button = Button(image=RIGHT_IMG, command=new_card)
yes_button.grid(column=0,row=1)

no_button = Button(image=WRONG_IMG, command=new_card)
no_button.grid(column=1, row=1)

new_card













window.mainloop()