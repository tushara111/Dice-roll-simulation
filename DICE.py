import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.geometry("500x360")
window.title("Dice Roll")

dice = [ "C:/Users/Dell/Downloads/dice/dice1.png", "C:/Users/Dell/Downloads/dice/dice2.png", "C:/Users/Dell/Downloads/dice/dice3.png", "C:/Users/Dell/Downloads/dice/dice4.png", "C:/Users/Dell/Downloads/dice/dice5.png", "C:/Users/Dell/Downloads/dice/dice6.png"]
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice))) #random.choice for tuple/list
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.Label(window,image=image1)
label2 = tk.Label(window,image=image2)

label1.image = image1
label2.image = image2

label1.place(x=40, y=300)
label2.place(x=300, y=300)

def dice_roll():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image= image1)
    label1.image = image1

    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image=image2)
    label2.image = image2

button = tk.Button(window, text= "ROLL", bg= "green", fg= "white", font= "Times 20 bold", command=dice_roll)
button.place(x= 230, y= 0)
window.mainloop()






