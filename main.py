import tkinter
from tkinter import ttk





window = tkinter.Tk()
window.title("Invoice")

frame = tkinter.Frame(window)
frame.pack(padx=20, pady=10)

fNameLabel = tkinter.Label(frame,text="First Name")
fNameLabel.grid(row=0, column=0)

lNameLabel = tkinter.Label(frame, text="Last Name")
lNameLabel.grid(row = 0, column=1)

fNameEntry = tkinter.Entry(frame)
fNameEntry.grid(row=1, column=0)

lNameEntry = tkinter.Entry(frame)
lNameEntry.grid(row=1, column=1)

pNumberLabel = tkinter.Label(frame, text="Phone Number")
pNumberLabel.grid(row=0, column=2)

pNumberEntry = tkinter.Entry(frame)
pNumberEntry.grid(row=1, column= 2)

quantityLabel = tkinter.Label(frame, text="Quantity")
quantityLabel.grid(row=2, column=0)
quantitySpinbox = tkinter.Spinbox(frame, from_=1, to=100)
quantitySpinbox.grid(row=3, column=0)

descriptionLabel = tkinter.Label(frame, text="Description")
descriptionLabel.grid(row=2, column=1)
descriptionEntry = tkinter.Entry(frame)
descriptionEntry.grid(row=3, column=1)

priceLabel = tkinter.Label(frame, text="Price")
priceLabel.grid(row=2, column=2)
priceSpinbox = tkinter.Spinbox(frame, from_=0.0, to=1000, increment=0.5)
priceSpinbox.grid(row=3, column=2)


window.mainloop()