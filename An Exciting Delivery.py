from tkinter import *
from time import *
from math import *
myInterface = Tk()
screen = Canvas(myInterface, width = 1000, height = 750, background = "white")
screen.pack()

#desk
screen.create_rectangle(0,625,1000,750, fill="#1A1406")
#desktop
screen.create_rectangle(125,50,875,550, fill="white", outline="black", width=20)
screen.create_rectangle(450,550,550,650, fill="black")
screen.create_polygon(450,625,375,650,375,675,625,675,625,650,550,625, fill="black")
#amazonheader
screen.create_rectangle(135,60,865,125, fill="#172230")
screen.create_rectangle(300,75,800,100, fill="white")
screen.create_rectangle(250,75,300,100, fill="#D6DBE0")
screen.create_rectangle(800,75,830,100, fill="#ff9900")
screen.create_text(192.5,87.5, text = "Amazon", font = "Arial 15 bold", fill="white")
screen.create_polygon(282,85,293,85,287,93, fill="#5A575F")
screen.create_text(270,87.5, text = "All", font = "Arial 10 bold", fill="#5A575F")
screen.create_oval(807,80,817,90, fill="#ff9900", outline="#172230", width=2)
screen.create_line(817,90,822,95, fill="#172230", width=2)
#productpage(this item is actually available online, not kidding)
screen.create_polygon(200,270,275,225,375,225,425,275,425,420,300,415,200,420,160,300, fill="#9E9AA9", smooth="true")
screen.create_text(471,175, text = "Emsco", font = "Arial 10 bold", fill="#146eb4")
screen.create_text(633,200, text = "Emsco Group Landscape Rock - Natural Granite", font = "Arial 12 bold", fill="black")
screen.create_text(644,225, text = "Appearance - Medium - Lightweight - Easy to Install", font = "Arial 12 bold", fill="black")
screen.create_line(450,250,825,250, fill="#9E9AA9")
screen.create_text(500,275, text="Price:              &", font="Arial 10 bold", fill="#9E9AA9")
screen.create_text(512,275, text="$29.28", font = "Arial 12 bold", fill="red")
screen.create_text(606,275, text="FREE SHIPPING", font="Arial 10 bold", fill="black")
screen.create_text(501,300, text="Color: Granite", font="Arial 12 bold", fill="black")
screen.create_text(500,325, text="Size: Medium", font="Arial 12 bold", fill="black")
screen.create_text(657,350, text="Natural texture and appearance, withstands extreme weather conditions", font="Arial 9 bold", fill="black")
screen.create_text(618,375, text="Easy to install and lightweight, covers up landscape utilities", font="Arial 9 bold", fill="black")
screen.create_rectangle(450,425,650,450, fill="#ff9900", outline="black")
screen.create_text(550,437.5, text="Add to Cart", font="Arial 11 bold", fill="black")
#cursor
x1 = 675
y1 = 475
x2 = 675
y2 = 500
x3 = 695
y3 = 493
x4 = 683
y4 = 497
x5 = 687
y5 = 495
x6 = 692
y6 = 504
x7 = 687
y7 = 505

triangle = screen.create_polygon(x1,y1,x2,y2,x3,y3, fill = "white", outline="black")
stick = screen.create_polygon(x4,y4,x5,y5,x6,y6,x7,y7, fill="white", outline="black")
screen.update()
sleep(1)
screen.delete(triangle,stick)

for f in range(1,15):
    triangle = screen.create_polygon(x1-3*f,y1-3*f,x2-3*f,y2-3*f,x3-3*f,y3-3*f, fill="white", outline="black")
    stick = screen.create_polygon(x4-3*f,y4-3*f,x5-3*f,y5-3*f,x6-3*f,y6-3*f,x7-3*f,y7-3*f, fill="white", outline="black") 
    screen.update()
    sleep(0.05)
    screen.delete(triangle,stick)

sleep(1)
    
#scenechange
screen.create_rectangle(0,0,1000,750, fill="white")
#globe
screen.create_oval(175,50,825,675, fill="skyblue")
screen.create_polygon(260,130,350,150,425,125,460,160,400,250,435,300,375,285,380,325,400,375,470,400,470,425,425,450,410,575,375,575,360,475,325,450,350,375,350,325,300,300, fill="green", smooth="true")
screen.create_polygon(550,325,575,275,625,275,675,300,715,300,700,365,705,500,675,525,625,530,630,425,565,375, fill="green", smooth="true")
screen.create_polygon(650,250,650,200,685,175,700,105,770,180,805,250,750,265,700,250, fill="green", smooth="true")
screen.create_polygon(450,625,525,650,625,660,500,680,390,664, fill="green", smooth="true")
#plane
screen.create_polygon(700,237.5,706,290,715,295,725,250,755,220,745,215, fill="black")
screen.create_polygon(715,257,725,243,755,260,750,273, fill="black")
screen.create_polygon(740,260,750,290,770,253, fill="black")
screen.create_polygon(715,260,680,235,685,225,720,235, fill="black", smooth="true")

#dottedpathway
width = 5
height = 5
ground = 250

for f in range(1,25):
    x1 = -5*f*3 + 715
    x2 = x1 + width
    y1 = .01*f**3 - 8*f + ground 
    y2 = y1 + height
    dot = screen.create_oval(x1,y1,x2,y2, fill="black")

    screen.update()
    sleep(0.05)
    
sleep(1)

#scenechange
screen.create_rectangle(0,0,1000,750, fill="#B3D2E9")
screen.create_rectangle(0,600,1000,800, fill="#272727")

#truck
width = 600
height = 350
ww = 130
for f in range(-20,65):
    #truckbody
    x1 = 20*f
    x2 = x1 + width
    y1 = 200
    y2 = y1 + height
    #upper left corner of left wheel
    x3 = x1-ww/2 + 50
    y3 = y2-ww/2

    #lower right corner of left wheel
    x4 = x1+ww/2 + 50
    y4 = y2+ww/2

    #upper left corner of right wheel
    x5 = x2-ww/2
    x6 = x2+ww/2

    #head of truck
    x7 = x2 + 100
    x8 = x7 + 75
    y5 = y1 + 150

    #window of truck
    y6 = y1 + 50
    y7 = y1 + 120
    x9 = x8 - 45

    #trucktext
    x10 = (x1 + x2)/2 
    x11 = (y1 + y2)/2
    
    truck = screen.create_rectangle(x1,y1,x2,y2, fill="#304A5E")
    head = screen.create_polygon(x2,y1,x7,y1,x8,y5,x8,y2,x2,y2, fill="yellow")
    window = screen.create_polygon(x2,y6,x7,y6,x9,y7,x2,y7, fill="white")
    wheel1 = screen.create_oval(x3,y3,x4,y4, fill="black")
    wheel2 = screen.create_oval(x5,y3,x6,y4, fill="black")
    text = screen.create_text(x10,x11, text = "UPS", font = "Helvetica 100 bold", fill="black")

    screen.update()
    sleep(0.03)
    screen.delete(truck,head,window,wheel1,wheel2,text)
    
#scenechange
screen.create_rectangle(0,0,1000,750, fill="white")
#porchconcrete
screen.create_rectangle(0,550,1000,750, fill="#D1CA99")
#door
screen.create_rectangle(200,0,800,550, fill="#0B0B0B")
screen.create_rectangle(200,0,300,550, fill="#161616")
screen.create_oval(225,50,275,125, fill="#E1E0D5")
#doormat
screen.create_rectangle(150,550,850,750, fill="#3E0A0A")


#package
height = 200
width = 350
y1 = 0
for f in range(0,22):
    #frontsquare
    y1 = y1 + 20
    y2 = y1 + height
    #sideparallelogram
    y3 = y1 - 75
    y4 = y2 - 75
    #text
    y5 = (y2+y1)/2
    
    front = screen.create_rectangle(400,y1,675,y2, fill="#B58E5C")
    side = screen.create_polygon(325,y3,325,y4,400,y2,400,y1, fill="#B58E5C", outline="black")
    top = screen.create_polygon(325,y3,400,y1,675,y1,600,y3, fill="#B58E5C", outline="black")
    text = screen.create_text(537.5,y5, text = "FRAGILE", font = "Helvetica 30 bold", fill="black")
    screen.update()
    sleep(0.01)
    screen.delete(front,side,top,text)
sleep(3)
screen.update()





