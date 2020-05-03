from tkinter import *

factors = []
window = Tk()
window.resizable(0,0)

def get_divisors(number):
    for i in range(1, number):
        if number % i == 0:
            factors.append(i)

    factors.append(number)
    for factor in factors:
        answers_box.insert("1.0",f"{factor} ")

def button1_clicked():
    answers_box.delete("1.0", END)
    del factors[:]
    get_divisors(int(get_num.get()))

get_num = Entry(window)
get_num.grid(row=0,column=0)

button1 = Button(window, text="get divisors", command=button1_clicked)
button1.grid(row=2,column=0)

answers_box = Text(window,width=20,height=10, bg="black", fg="green")
answers_box.grid(row=3,column=0)

window.mainloop()

