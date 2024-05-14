from tkinter import *

window = Tk()
window.title("Miles to KM")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

miles_label = Label(text="Miles")
miles_label.grid(column=3, row=0)

equals_label = Label(text="is equal to:")
equals_label.grid(columns=1, row=2)


entry = Entry(width=10)
entry.insert(END, string="Type Miles...")
entry.grid(column=2, row=0)

km_converted = Label(text=str(0))
km_converted.grid(column=2, row=2)

miles_label = Label(text="Kilometers")
miles_label.grid(column=3, row=2)


def button_pressed():
    miles_entered = int(entry.get())
    converted = converter(miles_entered)
    km_converted["text"] = str(converted)

# Not sure this part is ideal.
# Will see what she does later.


button = Button(text="Calculate", command=button_pressed)
button.grid(column=2, row=3)


def converter(miles):
    return miles*1.6


window.mainloop()
