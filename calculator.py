from tkinter import *

window = Tk()
window.title("Simple Calculator")

e = Entry(window, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_num = e.get()
    global first_number
    global math
    math = "addition"
    first_number = int(first_num)
    e.delete(0, END)

def button_subtract():
    first_num = e.get()
    global first_number
    global math
    math = "subtract"
    first_number = int(first_num)
    e.delete(0, END)

def button_multiply():
    first_num = e.get()
    global first_number
    global math
    math = "multiply"
    first_number = int(first_num)
    e.delete(0, END)

def button_divide():
    first_num = e.get()
    global first_number
    global math
    math = "divide"
    first_number = int(first_num)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, first_number + int(second_number))
    if math == "subtract":
        e.insert(0, first_number - int(second_number))
    if math == "multiply":
        e.insert(0, first_number * int(second_number))
    if math == "divide":
        e.insert(0, first_number / int(second_number))




# Defining buttons
button_1 = Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(window, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_plus = Button(window, text="+", padx=40, pady=20, command=button_add)
button_equal = Button(window, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(window, text="Clear", padx=81, pady=20, command=button_clear)

button_subtract = Button(window, text="-", padx=43, pady=20, command=button_subtract)
button_multiply = Button(window, text="*", padx=41, pady=20, command=button_multiply)
button_divide = Button(window, text="/", padx=41, pady=20, command=button_divide)

# Putting buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_plus.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)


window.mainloop()