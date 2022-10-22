from tkinter import *
import random, time


def roll_dice(event):
    global d_1, d_2
    for i in range(18):
        try:
            roll1 = random.choice(my_dice)
            roll2 = random.choice(my_dice)
            d_1 = PhotoImage(file=roll1)
            d_2 = PhotoImage(file=roll2)
            canvas1.create_image(280, 280, image=d_1, anchor="center")
            canvas1.create_image(620, 280, image=d_2, anchor="center")
            root.update()
            time.sleep(0.18)
        except RuntimeError:
            break


my_dice = ['images\\1.png', 'images\\2.png', 'images\\3.png', 'images\\4.png', 'images\\5.png', 'images\\6.png']
root = Tk()
root.geometry('900x600')
root.title('DICEPLAY')
root.resizable(height=False, width=False)
root.iconbitmap('images\\icon.ico')

background = PhotoImage(file='images\\table-rich-texture.png')
canvas1 = Canvas(root, width=900, height=600)
canvas1.pack()
canvas1.create_image(0, 0, image=background, anchor="nw")

root.bind('<1>', roll_dice)
roll_dice('event')
root.mainloop()
