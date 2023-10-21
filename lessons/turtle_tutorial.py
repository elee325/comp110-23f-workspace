"""Turtle Tutorial."""

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
bob: Turtle = Turtle()

colormode(255)

leo.speed(50)
leo.hideturtle()

bob.speed(70)
bob.hideturtle()

leo.penup()
leo.goto(-140, -100)
leo.pendown()

bob.penup()
bob.goto(-140, -100)
bob.pendown()

bob.color("black")
leo.color("pink")

side_length: int = 300



leo.begin_fill()

i: int = 0
while (i < 3):
    leo.forward(side_length)
    leo.left(120)
    i = i + 1

leo.end_fill()

i: int = 0
while (i < 70):
    bob.forward(side_length)
    bob.left(122)
    side_length = side_length * 0.97
    i = i + 1
    

done()