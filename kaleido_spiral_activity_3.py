import turtle
from itertools import cycle
colors=cycle(['maroon','gold','hot pink','light blue','thistle','lawn green'])
def draw_circle(size,angle,shift):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+12,angle+5,shift+3)
    
turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_circle(30,0,1)

