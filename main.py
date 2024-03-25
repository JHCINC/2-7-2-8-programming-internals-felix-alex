import tkinter as tk
from PIL import ImageTk, Image


window = tk.Tk()
window.title("Right Angle Calculator")
window.geometry("690x605")
window.config(bg='#2b2b2b')
window.resizable(width=False, height=False)

heading = tk.Label(window,text="Triangle Calculator!",font=('Arial',20),fg='#fafafa',bg='#2b2b2b')

traingle = Image.open("traingle.png")
test = ImageTk.PhotoImage(traingle)
trilabel = tk.Label(image=test)
trilabel.image = test

lang1 = tk.Label(text="Angle (°)")
eang1 = tk.Entry(window,width=5)
lang2 = tk.Label(text="Angle (°)")
eang2 = tk.Entry(window,width=5)

button = tk.Button(text="Calculate Sides/Angles", command='get_sides' and 'get_angles')

lang1.place(x=175,y=218)
eang1.place(x=175,y=248)
lang2.place(x=370,y=340)
eang2.place(x=450,y=375)
heading.place(x=20,y=20)
trilabel.place(x=20,y=70)
button.place(x=260,y= 550)

tk.mainloop()
