import turtle
from turtle import *


tur = turtle.Turtle()

# colors
hot_pink = (119, 44, 75)
dirty_blue = (52, 113, 124)
dark_lime = (151, 192, 62)

begin_fill()
tur.speed(1)
x = 5
while x < 5:
    tur.forward(200)
    tur.left(170)
    x += 1
end_fill()

turtle.done()