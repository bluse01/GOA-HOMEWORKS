from turtle import *

# box
width(5)
color("black")
for i in range(4):
    forward(200)
    left(90)

# door
color("gray")
penup()
goto(70, 0)
pendown()

left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)

# roof
color("black")
penup()
goto(200, 200)
pendown()

left(45)
forward(-143)
left(90)
forward(-140)

# windows
color("orange")
penup()
goto(175, 125)
pendown()

left(45)
for i in range(4):
    forward(50)
    left(90)

penup()
goto(75, 125)
pendown()

for i in range(4):
    forward(50)
    left(90)

exitonclick()