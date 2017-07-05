from tkinter import *
from random import *
myInterface = Tk()
screen = Canvas(myInterface, width=1000, height=700, background="white")
screen.pack()

#hardwood
x1 = 0
y1 = 575
x2 = 125
y2 = 600
for numplanks in range(0,8):
    screen.create_rectangle(x1,y1,x2,y2, fill="#3D382D", outline="#16130C")
    x1 = x2
    x2 = x2 + 125
    
x1 = 0
y1 = 600
x2 = 62.5
y2 = 625
for numplanks in range(0,9):
    screen.create_rectangle(x1,y1,x2,y2, fill="#3D382D", outline="#16130C")
    x1 = x2
    x2 = x2 + 125

x1 = 0
y1 = 625
x2 = 125
y2 = 650
for numplanks in range(0,8):
    screen.create_rectangle(x1,y1,x2,y2, fill="#3D382D", outline="#16130C")
    x1 = x2
    x2 = x2 + 125
    
x1 = 0
y1 = 650
x2 = 62.5
y2 = 675
for numplanks in range(0,9):
    screen.create_rectangle(x1,y1,x2,y2, fill="#3D382D", outline="#16130C")
    x1 = x2
    x2 = x2 + 125
    
x1 = 0
y1 = 675
x2 = 125
y2 = 700
for numplanks in range(0,8):
    screen.create_rectangle(x1,y1,x2,y2, fill="#3D382D", outline="#16130C")
    x1 = x2
    x2 = x2 + 125
#whitebrickwall
x1 = 0
y1 = 0
x2 = 25
y2 = 25
numtimes = 0
for numbricks in range(0,483):
    size = randint(50,150)
    shadowsize = randint(5,20)
    screen.create_rectangle(x1,y1,x2,y2, fill="white", outline="#9A9A9A", width=1.4)
    screen.create_rectangle(x1+3,y1+4,x1+shadowsize,y1+20, fill="#F3F3F3", outline="white")
    x1 = x2
    x2 = x2 + size
    numtimes = numtimes + 1
    
    if numtimes in ([21,42,63,84,105,126,147,168,189,210,231,252,273,294,315,336,357,378,399,420,441,462]):
        y1 = y1 + 25
        y2 = y2 + 25
        x1 = 0
        x2 = randint(20,100)
#window
screen.create_rectangle(125,75,375,375, fill="#BAD4DC", outline="#E7E7E6", width=20)
#water
screen.create_rectangle(135,300,365,375, fill="#BECAD3", outline="#BECAD3")
#mountainbase
screen.create_rectangle(135,275,365,300, fill="#5B636A")
screen.create_polygon(110,290,175,250,200,260,225,270,275,265,325,275,365,275, fill="#5B636A", smooth="true")
#rug
screen.create_oval(200,575,800,680, fill="#BCB183")
#ceilinglamp
screen.create_line(500,0,500,175, fill="black", width=2)
#bulb
screen.create_rectangle(475,100,525,150, fill="black")
screen.create_arc(455, 130, 545, 300, start=0, extent=180, fill="black")
screen.create_oval(455,205,545,221, fill="#F0D085")
#sofa
screen.create_rectangle(175,450,215,600, fill="grey")
screen.create_rectangle(215,555,785,600, fill="grey")
screen.create_rectangle(785,450,825,600, fill="grey")
screen.create_rectangle(250,423,750,500, fill="grey")
screen.create_polygon(215,450,250,425,250,500,215,525, fill="#707070", outline="black")
screen.create_polygon(210,425,250,425,215,450,175,450, fill="grey", outline="black")
screen.create_polygon(750,425,785,450,825,450,785,425, fill="grey", outline="black")
screen.create_polygon(750,425,750,500,785,525,785,450, fill="#707070", outline="black")
screen.create_polygon(250,500,750,500,785,525,785,560,215,560,215,525, fill="grey", outline="black")
#pillows
screen.create_oval(630,415,725,515, fill="#661C29")
screen.create_oval(275,415,370,515, fill="#661C29")
screen.create_oval(660,425,760,520, fill="#1A0509")
screen.create_oval(240,425,340,520, fill="#1A0509")
screen.create_oval(280,470,295,480, fill="black")
screen.create_oval(705,470,720,480, fill="black")
#tablelegs
screen.create_rectangle(640,525,650,615, fill="#AD7C09")
screen.create_rectangle(360,525,350,615, fill="#AD7C09")
screen.create_rectangle(350,605,650,615, fill="#AD7C09", outline="black")
#tabletop
screen.create_oval(350,500,650,550, fill="white", outline="black")
#books
screen.create_rectangle(450,515,550,525, fill="#DFC7D0")
screen.create_rectangle(465,505,535,515, fill="#AD6D85")
#flowervase
screen.create_polygon(490,450,510,450,515,506,485,506, fill="#504E4E", smooth="true")
screen.create_line(505,460,507,478,505,496, fill="white", smooth="true")
#tulips
for flowernum in range(0,15):
    x = randint(485, 525)
    y = randint(400, 450)
    c = choice(["#F490CA", "#E265A3","#C4317A"])
    screen.create_line(x-10,y-10,500,450, fill="#175100", width=2, smooth="true")
    screen.create_arc(x, y, x-20, y-40, start=180, extent=180, fill=c, outline="#490929")
#plantpot
screen.create_polygon(70,625,60,525,140,525,125,625, fill="white", outline="gray70")
screen.create_line(65,525,75,625, fill="#E2E2E2", width=10)
screen.create_oval(60,510,140,535, fill="#775221")
#plantstems
screen.create_line(100,400,100,525, width=5, fill="#175100")
screen.create_line(89,400,100,450,100,525, width=5, fill="#175100", smooth="true")
screen.create_line(86,435,105,460,100,525, width=5, fill="#175100", smooth="true")
screen.create_line(107,397,100,525, width=5, fill="#175100")
screen.create_line(140,440,115,475,100,525, width=5, fill="#175100", smooth="true")
screen.create_line(120,400,100,450, width=5, fill="#175100")
screen.create_line(112,400,100,450, width=5, fill="#175100")
screen.create_line(105,425,106,525, width=5, fill="#175100", smooth="true")
screen.create_line(78,460,90,480,97,525, width=5, fill="#175100", smooth="true")
#plantleaves
screen.create_polygon(75,225,70,275,75,350,100,425,125,350,125,275, fill="#1E6E15", smooth="true", outline="#072103")
screen.create_polygon(0,300,80,350,100,425, fill="#1E6E15", smooth="true", outline="#072103")
screen.create_polygon(225,250,100,425,100,350,125,340, fill="#1E6E15", smooth="true", outline="#072103")
screen.create_polygon(200,350,100,375,125,425, fill="#1E6E15", smooth="true", outline="#072103")
screen.create_polygon(225,380,140,375,100,420, fill="#1E6E15", smooth="true", outline="#072103")
screen.create_polygon(25,375,60,390,100,450,40,415, fill="#1E6E15", smooth="true", outline="#072103")
screen.create_polygon(260,425,160,420,125,450, fill="#1E6E15", smooth="true", outline="#072103")
screen.create_polygon(30,425,80,470,85,450,70,440, fill="#1E6E15", smooth="true", outline="#072103")
#frame1
screen.create_rectangle(625,175,750,375, fill="white", outline="black", width=10)
screen.create_rectangle(800,175,925,375, fill="white", outline="black", width=10)
#text
screen.create_text(687.5,250, text = "Work", font = "Helvetica 25 bold", fill="black")
screen.create_text(687.5,300, text = "Hard.", font = "Helvetica 25 bold", fill="black")
screen.create_text(862.5,250, text = "Play", font = "Helvetica 25 bold", fill="black")
screen.create_text(862.5,300, text = "Hard.", font = "Helvetica 25 bold", fill="black")
 
screen.update()




