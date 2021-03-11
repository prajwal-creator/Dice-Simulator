import tkinter
import random

root = tkinter.Tk()
root.geometry('600x600')
root.title('Roll Dice')

label = tkinter.Label(root, text='', font=('Helvetica', 260))

def roll_dice():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    dice1 = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685','\u2685','\u2685','\u2685']
    label.config(text=f'{random.choice(dice1)} {random.choice(dice)}')
    label.pack()

button = tkinter.Button(root, text='roll dice', foreground='blue', command=roll_dice)
button.place(x=265,y=450)
button.pack()
root.mainloop()
