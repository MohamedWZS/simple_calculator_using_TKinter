from tkinter import *

window = Tk()

# funcs
def display_num(num):
    current = screenEntry.get()                     # retrieve content in screenEntry input field
    screenEntry.delete(0, END)                      # clears the screenEntry input field
    screenEntry.insert(0, str(current) + str(num))

def clear_num():
    screenEntry.delete(0, END)                      # clears the screenEntry input field

# create number screen
screenEntry = Entry(window, width = 36)
screenEntry.grid(row=0, column=0, columnspan=3)

# define numbers
num7 = Button(window, text="7", width = 9, command=lambda: display_num(7)).grid(row=1, column=0)
num8 = Button(window, text="8", width = 9, command=lambda: display_num(8)).grid(row=1, column=1)
num9 = Button(window, text="9", width = 9, command=lambda: display_num(9)).grid(row=1, column=2)

num4 = Button(window, text="4", width = 9, command=lambda: display_num(4)).grid(row=2, column=0)
num5 = Button(window, text="5", width = 9, command=lambda: display_num(5)).grid(row=2, column=1)
num6 = Button(window, text="6", width = 9, command=lambda: display_num(6)).grid(row=2, column=2)

num1 = Button(window, text="1", width = 9, command=lambda: display_num(1)).grid(row=3, column=0)
num2 = Button(window, text="2", width = 9, command=lambda: display_num(2)).grid(row=3, column=1)
num3 = Button(window, text="3", width = 9, command=lambda: display_num(3)).grid(row=3, column=2)

num0 = Button(window, text="0", width = 9, command=lambda: display_num(0)).grid(row=4, column=0)
clear = Button(window, text="C", width = 9, command=clear_num).grid(row=4, column=2)
equal = Button(window, text="=")

plus = Button(window, text="+", width = 9).grid(row=4, column=1)

window.mainloop()