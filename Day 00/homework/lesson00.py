from turtle import *

def draw_square(x, y, penwidth, pencolor):
    pensize(penwidth)
    color(pencolor)
    penup()
    setx(x)
    sety(y)
    pendown()
    for _ in range(4):
        forward(200)
        left(90)

def draw_door(x, y, penwidth, pencolor):
    pensize(penwidth)
    color(pencolor)
    penup()
    setx(x)
    sety(y)
    pendown()

    begin_fill()
    left(90)
    forward(100)
    right(90)
    forward(60)
    right(90)
    forward(100)
    end_fill()

def draw_roof(x, y, penwidth, pencolor):
    pensize(penwidth)
    color(pencolor)
    penup()
    setx(x)
    sety(y)
    pendown()

    begin_fill()
    left(45)
    forward(-142)
    left(90)
    forward(-140)
    end_fill()

def draw_window(x, y, penwidth, pencolor):
    pensize(penwidth)
    color(pencolor)
    penup()
    setx(x)
    sety(y)
    pendown()

    for _ in range(4):
        forward(50)
        left(90)


draw_square(0, 0, 5, "black")
draw_door(70, 0, 5, "black")
draw_roof(200, 200, 5, "black")
left(45)
draw_window(175, 125, 5 , "black")
draw_window(75, 125, 5 , "black")

exitonclick()