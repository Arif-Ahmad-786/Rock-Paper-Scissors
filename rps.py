from tkinter import *
import random

root = Tk()
root.geometry("750x750")
root.title("Stone Paper Scissor Game")


button_bg = "#4CAF50"
button_fg = "#FFFFFF"
label_bg = "#E0E0E0"
font_medium = ("Arial", 12)
font_large = ("Arial", 16, "bold")

myframe = LabelFrame(root, text="STONE PAPER SCISSOR", font=font_large, padx=20, pady=20)
myframe.pack(fill="both", expand=True)

label1 = Label(myframe, text="STONE PAPER SCISSOR", font=font_large)
label1.grid(row=0, column=1, columnspan=3, pady=20, sticky="nsew")

c = ["ROCK", "PAPER", "SCISSOR"]
a = ""
comp = 0
you = 0

def scissor():
    global a
    a = "SCISSOR"
    b = random.choice(c)
    label5.config(text=a)
    label3.config(text=b)
    winlose(a, b)

def rock():
    global a
    a = "ROCK"
    b = random.choice(c)
    label5.config(text=a)
    label3.config(text=b)
    winlose(a, b)

def paper():
    global a
    a = "PAPER"
    b = random.choice(c)
    label5.config(text=a)
    label3.config(text=b)
    winlose(a, b)

def winlose(a, b):
    global comp
    global you
    if a == b:
        pass
    elif (a == "ROCK" and b == "SCISSOR") or (a == "PAPER" and b == "ROCK") or (a == "SCISSOR" and b == "PAPER"):
        you += 1
    else:
        comp += 1
    label8.config(text=str(comp))
    label9.config(text=str(you))
    disable_buttons()

def disable_buttons():
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    button3.config(state=DISABLED)

def replay():
    global a
    a = ""
    label5.config(text="                   ")
    label3.config(text="                   ")
    button1.config(state=NORMAL)
    button2.config(state=NORMAL)
    button3.config(state=NORMAL)


photo = PhotoImage(file=r"E:\codesoft\codes\q3\scissor.png").subsample(5, 5)
button1 = Button(myframe, text="SCISSOR", image=photo, command=scissor)
button1.grid(row=1, column=0, padx=20, pady=20)

photo2 = PhotoImage(file=r"E:\codesoft\codes\q3\paper.png").subsample(5, 5)
button2 = Button(myframe, text="PAPER", image=photo2, command=paper)
button2.grid(row=1, column=1, padx=20, pady=20)

photo3 = PhotoImage(file=r"E:\codesoft\codes\q3\rock.png").subsample(2, 2)
button3 = Button(myframe, text="ROCK", image=photo3, command=rock)
button3.grid(row=1, column=2, padx=20, pady=20)

label2 = Label(myframe, text="Computer chooses:", font=font_medium)
label2.grid(row=2, column=0, pady=10, sticky="e")
label3 = Label(myframe, text="                   ", bg="pink", font=font_medium, relief="sunken")
label3.grid(row=2, column=1, pady=10, sticky="nsew", columnspan=2)

label4 = Label(myframe, text="You choose:", font=font_medium)
label4.grid(row=3, column=0, pady=10, sticky="e")
label5 = Label(myframe, text="                   ", bg="sky blue", font=font_medium, relief="sunken")
label5.grid(row=3, column=1, pady=10, sticky="nsew", columnspan=2)


label6 = Label(myframe, text="COMPUTER", font=font_medium)
label6.grid(row=4, column=0, pady=20)
label7 = Label(myframe, text="YOU", font=font_medium)
label7.grid(row=4, column=2, pady=20)

label8 = Label(myframe, text="0", bg="pink", font=font_large, relief="sunken")
label8.grid(row=5, column=0, pady=10)
label9 = Label(myframe, text="0", bg="sky blue", font=font_large, relief="sunken")
label9.grid(row=5, column=2, pady=10)


button4 = Button(myframe, text="Play Again", command=replay, bg=button_bg, fg=button_fg, font=font_medium)
button4.grid(row=6, column=0, pady=20, padx=20, sticky="nsew")
button5 = Button(myframe, text="EXIT", command=root.destroy, bg="#f44336", fg=button_fg, font=font_medium)
button5.grid(row=6, column=2, pady=20, padx=20, sticky="nsew")


myframe.grid_columnconfigure(0, weight=1)
myframe.grid_columnconfigure(1, weight=1)
myframe.grid_columnconfigure(2, weight=1)

root.mainloop()
