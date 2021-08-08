import tkinter

window = tkinter.Tk()
window.title('Distance Calculator')
window.minsize(250, 120)
window.config(padx=30, pady=10)

label_miles = tkinter.Label(text='Miles',font=('Times New Roman', 12, 'bold'))
label_miles.grid(column=2, row=0)

label_equal = tkinter.Label(text='is equal to',font=('Times New Roman', 12, 'bold'))
label_equal.grid(column=0, row=1)

label_conversion = tkinter.Label(text='0',font=('Times New Roman', 12, 'bold'))
label_conversion.grid(column=1, row=1)

label_km = tkinter.Label(text='Km',font=('Times New Roman', 12, 'bold'))
label_km.grid(column=2, row=1)


def convert():
    mile = int(input.get())
    km_output = mile * 1.609
    print(km_output)
    label_conversion.config(text=km_output)
    return km_output

input = tkinter.Entry(width=9)
input.grid(column=1, row=0)

button = tkinter.Button(text='Convert', font=('Times New Roman', 12), background='green', activebackground=('lime'), command=convert)
button.grid(column=1, row=2)



window.mainloop()