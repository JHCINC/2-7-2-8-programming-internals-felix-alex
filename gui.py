import tkinter as tk
from PIL import ImageTk, Image


window = tk.Tk()
window.title("Right Angle Calculator")
window.geometry("1000x800")
window.config(bg='#2b2b2b')
window.resizable(width=False, height=False)

heading = tk.Label(window,text="Triangle Calculator!",font=('Arial',20),fg='#fafafa',bg='#2b2b2b')

traingle = Image.open("traingle.png")
test = ImageTk.PhotoImage(traingle)
trilabel = tk.Label(image=test)
trilabel.image = test

button = tk.Button(text="Calculate Sides/Angles", command='get_sides' and 'get_angles')

heading.place(x=20,y=20)
trilabel.place(x=20,y=70)
button.place(x=250, y= 600)

tk.mainloop()
