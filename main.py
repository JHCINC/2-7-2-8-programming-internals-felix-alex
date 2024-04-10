# import block
import math
from PIL import ImageTk, Image
import tkinter as tk

# function to calculate the side lengths and angles
def get_sidesandangles():
    global s1, s2, s3, a1, a2
    # validate input
    validate(esid1.get(), esid2.get(), esid3.get(), eang1.get(), eang2.get())

    # use one angle to find the other if possible
    if a1 == 0 and a2 != 0:
        a1 = 90 - a2
    if a2 == 0 and a1 != 0:
        a2 = 90 - a1

    # if all possible calculations have been made,
    # display results and exit function
    if s1 == 0 and s2 == 0 and s3 == 0:
        ansdisplay(s1, s2, s3, a1, a2)
        return

    # use the sine rule to find unknown sides if possible,
    # then display and exit
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
        ansdisplay(s1, s2, s3, a1, a2)
        return

    # if all possible calculations have been made,
    # display results and exit funtion
    if not (
        (s1 != 0 and s2 != 0) or (s1 != 0 and s3 != 0) or (s2 != 0 and s3 != 0)
    ):
        ansdisplay(s1, s2, s3, a1, a2)
        return

    # use pythagorean theorem to find unknown sides if possible,
    # then display and exit
    if s1 == 0:
        s1 = math.sqrt(s2**2 - s3**2)
    elif s2 == 0:
        s2 = math.sqrt(s1**2 + s3**2)
    else:
        s3 = math.sqrt(s2**2 - s1**2)

    # use the sine rule to find unknown sides if possible,
    # then display and exit
    sinerule = s2/math.sin(math.radians(90))
    if s1 == 0:
        s1 = sinerule*math.sin(math.radians(a2))
    if s2 == 0:
        s2 = sinerule*math.sin(math.radians(90))
    if s3 == 0:
        s3 = sinerule*math.sin(math.radians(a1))

    # use sine rule to find unknown angles, then display and exit
    if a1 == 0:
        a1 = math.degrees(math.asin(s3/s2))
    if a2 == 0:
        a2 = math.degrees(math.asin(s1/s2))

    ansdisplay(s1, s2, s3, a1, a2)
    return


# function to display the results
def ansdisplay(a, b, c, d, e):

    # round results to 3dp
    sa = round(float(a), 3)
    sb = round(float(b), 3)
    sc = round(float(c), 3)
    aa = round(float(d), 3)
    ab = round(float(e), 3)

    # replace 0's in results with unknown, as 0 was used as a placeholder
    if sa == 0:
        sa = 'Unknown'
    if sb == 0:
        sb = 'Unknown'
    if sc == 0:
        sc = 'Unknown'
    if aa == 0:
        aa = 'Unknown'
    if ab == 0:
        ab = 'Unknown'

    # replace the input boxes with the results
    esid1.delete(0, tk.END)
    esid1.insert(0, str(sa))
    esid2.delete(0, tk.END)
    esid2.insert(0, str(sb))
    esid3.delete(0, tk.END)
    esid3.insert(0, str(sc))
    eang1.delete(0, tk.END)
    eang1.insert(0, str(aa))
    eang2.delete(0, tk.END)
    eang2.insert(0, str(ab))


# function to validate input
def validate(a, b, c, d, e):
    global s1, s2, s3, a1, a2
    try:
        s1 = float(a)
    except ValueError:
        s1 = 0
    try:
        s2 = float(b)
    except ValueError:
        s2 = 0
    try:
        s3 = float(c)
    except ValueError:
        s3 = 0
    try:
        a1 = float(d)
    except ValueError:
        a1 = 0
    try:
        a2 = float(e)
    except ValueError:
        a2 = 0


enter = False

# create window for program
window = tk.Tk()
window.title("Right Angle Calculator")
window.geometry("690x605")
window.config(bg='#2b2b2b')
window.resizable(width=False, height=False)

# title text
heading = tk.Label(
    window,
    text="Right-Angled Triangle Calculator!",
    font=('Arial', 20),
    fg='#fafafa',
    bg='#2b2b2b'
)

# image for triangle diagram
traingle = Image.open("traingle.png")
test = ImageTk.PhotoImage(traingle)
trilabel = tk.Label(image=test)
trilabel.image = test

# labels and input boxes for angles
lang1 = tk.Label(
    text="Angle (°)",
    bg='#2b2b2b',
    fg='#fafafa',
    font=('Arial', 12)
)
eang1 = tk.Entry(window, width=8)
lang2 = tk.Label(
    text="Angle (°)",
    bg='#2b2b2b',
    fg='#fafafa',
    font=('Arial', 12)
)
eang2 = tk.Entry(window, width=8)

# labels and input boxes for sides
lsid1 = tk.Label(
    text="Side (u)",
    bg='#2b2b2b',
    fg='#fafafa',
    font=('Arial', 12)
)
esid1 = tk.Entry(window, width=8)
lsid2 = tk.Label(
    text="Side (u)",
    bg='#2b2b2b',
    fg='#fafafa',
    font=('Arial', 12)
)
esid2 = tk.Entry(window, width=8)
lsid3 = tk.Label(
    text="Side (u)",
    bg='#2b2b2b',
    fg='#fafafa',
    font=('Arial', 12)
)
esid3 = tk.Entry(window, width=8)

# instructions
ins1 = tk.Label(
    text="1. Type in the white textboxes any known angles or side lengths.",
    bg='#2b2b2b',
    fg='#fafafa',
    font=('Arial', 12)
)
ins2 = tk.Label(
    text="2. Click the button to use the entered values to find the missing ones.",
    bg='#2b2b2b',
    fg='#fafafa',
    font=('Arial', 12)
)

# button to calculate sides and angles
button = tk.Button(text="Calculate Sides/Angles", command=get_sidesandangles)

# exit button
exit = tk.Button(text="Leave Program :(", command=exit)

# placing all the widgets
lang1.place(x=175, y=252)
eang1.place(x=175, y=222)
lang2.place(x=355, y=372)
eang2.place(x=435, y=375)

lsid1.place(x=55, y=250)
esid1.place(x=55, y=280)
lsid2.place(x=400, y=200)
esid2.place(x=400, y=230)
lsid3.place(x=325, y=480)
esid3.place(x=320, y=450)

ins1.place(x=30, y=80)
ins2.place(x=30, y=522)
heading.place(x=20, y=20)
trilabel.place(x=20, y=70)
button.place(x=260, y=550)
exit.place(x=540, y=20)


# mainloop
tk.mainloop()
