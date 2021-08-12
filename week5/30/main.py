import tkinter

window = tkinter.Tk()
window.title('Password Manager')
window.config(padx=50, pady=50,)
canvas = tkinter.Canvas(height=200, width=200)
bgImage = tkinter.PhotoImage(file='logo.png', width=200, height=200,)
canvas.create_image(100,100,image=bgImage)
canvas.grid(column=1, row =0 )

#Label Fields
site_label = tkinter.Label(text='Website:')
site_label.grid(column=0, row=1)
user_label = tkinter.Label(text='Email/Username:')
user_label.grid(column=0, row=2)
pass_label = tkinter.Label(text='Password:')
pass_label.grid(column=0, row=3)

#Input Fields
site_input = tkinter.Entry(width=35)
site_input.grid(column=1, row=1, columnspan=2)
user_input = tkinter.Entry(width=35)
user_input.grid(column=1, row=2, columnspan=2)
pass_input = tkinter.Entry(width=20)
pass_input.place(x=151, y=250)

#Button Fields
gen_pass_but = tkinter.Button(text='Generate Password', command=print('password'))
gen_pass_but.grid(column=2, row=3)
add_entry_but = tkinter.Button(text='Add Entry', command=print('Added'), width=36)
add_entry_but.grid(column=1, row=4, columnspan=2)


window.mainloop()