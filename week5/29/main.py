from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
rep_checks = ''

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_session():
    global reps, rep_checks
    reps = 0
    rep_checks=''
    checks.config(text=rep_checks)
    canvas.itemconfig(timer_text, text='00:00')
    


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    if reps == 8:
        count_down(LONG_BREAK_MIN * 60)
    if reps % 2 == 0:
        count_down(WORK_MIN * 60)
    else:
        count_down(SHORT_BREAK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global reps, rep_checks

    min = math.floor(count /60)
    sec = count % 60

    if sec < 10:
        sec = f'0{sec}'
    canvas.itemconfig(timer_text, text=f'{min}:{sec}')
    if count > 0:
        window.after(1000,count_down, count - 1)
    else:
        reps +=1
        if reps % 2 == 0:
            rep_checks +='✓'
        checks.config(text=rep_checks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height= 224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image = tomato)
timer_text = canvas.create_text(101, 130,text='00:00', font=(FONT_NAME, 20,),fill='white')

header = Label(text='Timer', bg= YELLOW, font=(FONT_NAME, 32))
header.pack()


start_but = Button(text='Start',command=start_timer)
start_but.place(x=-30,y=275)

res_but = Button(text='Reset', command=reset_session)
res_but.place(x=170,y=275)


canvas.pack()
checks = Label(text='', font=(FONT_NAME, 24), fg=GREEN, bg=YELLOW)
checks.pack()


window.mainloop()