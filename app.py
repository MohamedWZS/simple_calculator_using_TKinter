from cmath import sqrt
from tkinter import *

window = Tk()

# global variables
mode = ""

# funcs
def display_num(num):
    current = screenEntry.get()                     # retrieve content in screenEntry input field
    screenEntry.delete(0, END)                      # clears the screenEntry input field
    screenEntry.insert(0, str(current) + str(num))  # displays on input field screen

def clear_num():
    screenEntry.delete(0, END)

def add_nums():
    global mode
    mode = "add"                                    # set calc mode to add

    firstNum = screenEntry.get()
    global fNum                                     # create global var that holds the firsNum
    fNum = int(firstNum)
    
    screenEntry.delete(0, END)

def sub_nums():
    global mode
    mode = "sub"                                    # set calc mode to sub

    firstNum = screenEntry.get()
    global fNum                                     # create global var that holds the firsNum
    fNum = int(firstNum)

    screenEntry.delete(0, END)

def mult_nums():
    global mode
    mode = "mult"                                   # set calc mode to mult

    firstNum = screenEntry.get()
    global fNum                                     # create global var that holds the firsNum
    fNum = int(firstNum)

    screenEntry.delete(0, END)

def div_nums():
    global mode
    mode = "div"                                    # set calc mode to div

    firstNum = screenEntry.get()
    global fNum                                     # create global var that holds the firsNum
    fNum = int(firstNum)

    screenEntry.delete(0, END)

def rec_nums():
    global mode
    mode = "rec"                                    # set calc mode to reciprocal

    firstNum = int(screenEntry.get())
    global fNum
    fNum = 1/firstNum

    screenEntry.delete(0, END)
    screenEntry.insert(0, fNum)

def square_nums():
    global mode 
    mode = "square"                                 # set calc mode to square

    firstNum = int(screenEntry.get())
    global fNum
    fNum = firstNum ** 2

    screenEntry.delete(0, END)                      # clears input field screen
    screenEntry.insert(0, fNum)                     # display output on input field screen

def sqrt_nums():
    global mode 
    mode = "square"                                 # set calc mode to sqrt

    firstNum = int(screenEntry.get())
    global fNum
    fNum = sqrt(firstNum).real

    screenEntry.delete(0, END)                      # clears input field screen
    screenEntry.insert(0, fNum)                     # display output on input field screen

def equal():
    secondtNum = int(screenEntry.get())
    screenEntry.delete(0, END)

    if mode == "add":                               # check mode
        result = fNum + secondtNum                  # adds two numbers
    elif mode == "sub":
        result = fNum - secondtNum                  # subs two numbers
    elif mode == "mult":
        result = fNum * secondtNum                  # mult two numbers
    else:
        result = fNum / secondtNum                  # divides two numbers

    screenEntry.insert(0, result)                   # display on input field screen

# create number screen
screenEntry = Entry(window, width = 50)
screenEntry.grid(row=0, column=0, columnspan=4)

# define numbers and modes
reciprocal = Button(window, text="1/x", width=9, pady=5, command=rec_nums).grid(row=2, column=0)
square = Button(window, text="x^2", width = 9, pady=5, command=square_nums).grid(row=2, column=1)
squareroot = Button(window, text="root", width = 9, pady=5, command=sqrt_nums).grid(row=2, column=2)
divide = Button(window, text="/", width = 9, pady=5, command=div_nums).grid(row=2, column=3)

num7 = Button(window, text="7", width=9, pady=5, command=lambda: display_num(7)).grid(row=3, column=0)
num8 = Button(window, text="8", width=9, pady=5, command=lambda: display_num(8)).grid(row=3, column=1)
num9 = Button(window, text="9", width=9, pady=5, command=lambda: display_num(9)).grid(row=3, column=2)
multiply = Button(window, text="x", width = 9, pady=5, command=mult_nums).grid(row=3, column=3)

num4 = Button(window, text="4", width=9, pady=5, command=lambda: display_num(4)).grid(row=4, column=0)
num5 = Button(window, text="5", width=9, pady=5, command=lambda: display_num(5)).grid(row=4, column=1)
num6 = Button(window, text="6", width=9, pady=5, command=lambda: display_num(6)).grid(row=4, column=2)
subtract = Button(window, text="-", width = 9, pady=5, command=sub_nums).grid(row=4, column=3)

num1 = Button(window, text="1", width=9, pady=5, command=lambda: display_num(1)).grid(row=5, column=0)
num2 = Button(window, text="2", width=9, pady=5, command=lambda: display_num(2)).grid(row=5, column=1)
num3 = Button(window, text="3", width=9, pady=5, command=lambda: display_num(3)).grid(row=5, column=2)
plus = Button(window, text="+", width = 9, pady=5, command=add_nums).grid(row=5, column=3)

num0 = Button(window, text="0", width=9, pady=5, command=lambda: display_num(0)).grid(row=6, column=0)
clear = Button(window, text="C", width=9, pady=5, command=clear_num).grid(row=6, column=1)
equality = Button(window, text="=", width=20, pady=5, command=equal).grid(row=6, column=2, columnspan=2)

window.mainloop()