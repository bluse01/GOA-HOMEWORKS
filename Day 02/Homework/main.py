from turtle import *

def draw_cage(check, length, ps, color, for_tower = False):
    pencolor(color)
    pensize(ps)

    match check:
        case "right":
            right(90)

            for i in range(length):
                forward(15)
                right(90)

                forward(15)
                left(90)

                forward(15)
                left(90)

                forward(15)
                right(90)

            if for_tower:
                forward(15)
                right(90)
                forward(450)

        case "left":
            left(90)

            for i in range(length):
                forward(15)
                left(90)

                forward(15)
                right(90)

                forward(15)
                right(90)
                
                forward(15)
                left(90)

            if for_tower:
                forward(15)
                left(90)
                forward(450)

def draw_watchtower(x, y, ps, color, check, for_tower):
    pencolor(color)
    pensize(ps)
    penup()
    setx(x)
    sety(y)
    pendown()

    left(90)
    forward(450)

    draw_cage(check, 4, 3, "black", for_tower)

def draw_floor(x, y, ps, color):
    pencolor(color)
    pensize(ps)
    penup()
    setx(x)
    sety(y)
    pendown()

    forward(-500)
    forward(1000)

def draw_base(x, y, ps, color):
    pencolor(color)
    pensize(ps)
    penup()
    setx(x)
    sety(y)
    pendown()

    draw_cage("left", 24, 3, "black", None)
    forward(10)

def draw_gate(cord, ps, color):
    pencolor(color)
    pensize(ps)

    left(90)

    for i in cord:
        x, y = i
        
        penup()
        setx(x)
        sety(y)
        pendown()

        forward(130)

    circle(x, 180)
    left(90)
    forward(x + x)

    setx(0)
    right(90)
    forward(130)
    
def draw_brick(x, y, ps, pencolor, fill_color, width, height):
    penup()
    setx(x)
    sety(y)
    pendown()

    color(pencolor, fill_color)
    pensize(ps)

    begin_fill()
    for _ in range(2):
        forward(width)
        right(90)
        forward(height)
        right(90)
    end_fill()

# I am pretty proud of this func
def draw_texture(x_coords, y_coords):

    brick_width = 30
    brick_height = 15

    x_min, x_max = x_coords
    y_min, y_max = y_coords

    cols = (x_max - x_min) // brick_width
    rows = (y_max - y_min) // brick_height

    for row in range(rows):
        for col in range(cols):

            x = x_min + col * brick_width
            y = y_max - row * brick_height
            
            draw_brick(x, y, 1, "black", "gray", brick_width, brick_height)

setup(width=1200, height=800)
speed(0)
draw_floor(0, -300, 3, "gray")
draw_watchtower(-500, -300, 3, "black", "right", True)
left(90)
draw_watchtower(500, -300, 3, "black", "left", True)
draw_base(-365, -50, 3, "black")
draw_gate([(-70, -300),(70, -300)] , 3, "black")
left(90)
draw_texture([-495, -360], [-300, 130])
draw_texture([370, 505], [-300, 130])

mainloop()