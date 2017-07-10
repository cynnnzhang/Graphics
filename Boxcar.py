from tkinter import *
from time import *
myInterface = Tk()
s = Canvas(myInterface, width=1000, height=700, background="white")
s.pack()

x1 = 100
carWidth = 150
carHeight = 80
ww = 40
top = 60
for f in range (0,200):
    box = s.create_rectangle(x1,top,x1+carWidth,top+carHeight, fill="blue")
    wheel1 = s.create_oval(x1-ww/2,top+carHeight-ww/2,x1+ww/2,top+carHeight+ww/2, fill="navy")
    wheel2 = s.create_oval(x1+carWidth-ww/2,top+carHeight-ww/2,x1+carWidth+ww/2,top+carHeight+ww/2, fill="navy")

    s.update()
    sleep(0.03)
    s.delete(box, wheel1, wheel2)
    x1 = x1 + 5
    top = top + 3
