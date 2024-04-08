import math
from PIL import ImageTk, Image
import tkinter as tk

def get_sidesandangles():
  global s1, s2, s3, a1, a2
  try:
    s1= float(esid1.get())
  except ValueError:
    s1= 0
  try:
    s2= float(esid2.get())
  except ValueError:
    s2= 0
  try:
    s3= float(esid3.get())
  except ValueError:
    s3= 0
  try:
    a1= float(eang1.get())
  except ValueError:
    a1= 0
  try:
    a2= float(eang2.get())
  except ValueError:
    a2= 0
  
  if a1 == 0 and a2 != 0:
    a1 = 90 - a2
  if a2 == 0 and a1 != 0:
    a2 = 90 - a1

  if s1 == 0 and s2 == 0 and s3 == 0:
    ansdisplay()
    return

  if a1 != 0 and a2 != 0 and not (s1 != 0 and s2 != 0 and s3 != 0):
    if s1 != 0:
      sineruleuse = s1/math.sin(math.radians(a2))
    elif s2 != 0:
      sineruleuse = s2/math.sin(math.radians(90))
    else:
      sineruleuse = s3/math.sin(math.radians(a1))

    if s1 == 0:
      s1 = sineruleuse*math.sin(math.radians(a2))
    if s2 == 0:
      s2 = sineruleuse*math.sin(math.radians(90))
    if s3 == 0:
      s3 = sineruleuse*math.sin(math.radians(a1))
    ansdisplay()
    return

  if not ((s1 != 0 and s2 != 0) or (s1 != 0 and s3 != 0) or (s2 != 0 and s3 != 0)):
    ansdisplay()
    return

  if s1 == 0:
    s1 = math.sqrt(s2**2 - s3**2)
  elif s2 == 0:
    s2 = math.sqrt(s1**2 + s3**2)
  else:
    s3 = math.sqrt(s2**2 - s1**2)

  sinerule = s2/math.sin(math.radians(90))
  if s1 == 0:
    s1 = sinerule*math.sin(math.radians(a2))
  if s2 == 0:
    s2 = sinerule*math.sin(math.radians(90))
  if s3 == 0:
    s3 = sinerule*math.sin(math.radians(a1))

  if a1 == 0:
    a1 = math.degrees(math.asin(s3/s2))
  if a2 == 0:
    a2 = math.degrees(math.asin(s1/s2))
  
  ansdisplay()
  return

def ansdisplay():
  global s1, s2, s3, a1, a2

  s1 = round(float(s1), 3)
  s2 = round(float(s2), 3)
  s3 = round(float(s3), 3)
  a1 = round(float(a1), 3)
  a2 = round(float(a2), 3)
  
  if s1 == 0:
    s1 = 'Unknown'
  if s2 == 0:
    s2 = 'Unknown'
  if s3 == 0:
    s3 = 'Unknown'
  if a1 == 0:
    a1 = 'Unknown'
  if a2 == 0:
    a2 = 'Unknown'
  
  esid1.delete(0, tk.END)
  esid1.insert(0, str(s1))
  esid2.delete(0, tk.END)
  esid2.insert(0, str(s2))
  esid3.delete(0, tk.END)
  esid3.insert(0, str(s3))
  eang1.delete(0, tk.END)
  eang1.insert(0, str(a1))
  eang2.delete(0, tk.END)
  eang2.insert(0, str(a2))

enter = False

window = tk.Tk()
window.title("Right Angle Calculator")
window.geometry("690x605")
window.config(bg='#2b2b2b')
window.resizable(width=False, height=False)

heading = tk.Label(window,text="Right-Angled Triangle Calculator!",font=('Arial',20),fg='#fafafa',bg='#2b2b2b')

traingle = Image.open("traingle.png")
test = ImageTk.PhotoImage(traingle)
trilabel = tk.Label(image=test)
trilabel.image = test

lang1 = tk.Label(text="Angle (°)", bg='#2b2b2b', fg='#fafafa', font=('Arial',12))
eang1 = tk.Entry(window,width=8)
lang2 = tk.Label(text="Angle (°)", bg='#2b2b2b', fg='#fafafa', font=('Arial',12))
eang2 = tk.Entry(window,width=8)

lsid1 = tk.Label(text="Side (u)", bg='#2b2b2b', fg='#fafafa', font=('Arial',12))
esid1 = tk.Entry(window,width=8)
lsid2 = tk.Label(text="Side (u)", bg='#2b2b2b', fg='#fafafa', font=('Arial',12))
esid2 = tk.Entry(window,width=8)
lsid3 = tk.Label(text="Side (u)", bg='#2b2b2b', fg='#fafafa', font=('Arial',12))
esid3 = tk.Entry(window,width=8)

ins1 = tk.Label(text="1. Type in the white textboxes any known angles or side lengths.", bg='#2b2b2b', fg='#fafafa', font=('Arial',12))
ins2 = tk.Label(text="2. Click the button to use the entered values to find the missing ones.", bg='#2b2b2b', fg='#fafafa', font=('Arial',12))

button = tk.Button(text="Calculate Sides/Angles", command=get_sidesandangles)

exit = tk.Button(text="Leave Program :(", command=exit)

lang1.place(x=175,y=248)
eang1.place(x=175,y=218)
lang2.place(x=370,y=370)
eang2.place(x=450,y=375)

lsid1.place(x=55,y=250)
esid1.place(x=65,y=280)
lsid2.place(x=395,y=200)
esid2.place(x=400,y=230)
lsid3.place(x=325,y=480)
esid3.place(x=330,y=450)

ins1.place(x=30,y=80)
ins2.place(x=30,y=522)
heading.place(x=20,y=20)
trilabel.place(x=20,y=70)
button.place(x=260,y= 550)
exit.place(x=540,y=20)



tk.mainloop()
