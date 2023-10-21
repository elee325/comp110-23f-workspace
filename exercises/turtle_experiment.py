"""Turtle Drawing: City of Stars"""

__author__ = "730468571"

from turtle import Turtle, colormode, done, tracer, update
from random import randint

def main() -> None:
    """The entrypoint of my scene."""
    tracer(0, 0) # Disable delay in tracing
    colormode(255)
    # Declare your Turtle variable(s) here.
    lala: Turtle = Turtle()
    lala.speed(0)
    lala.hideturtle()

    lala.screen.bgcolor(37, 35, 128)

# Drawing the stars randomly.
    i: int = 0
    while i < 30:
        draw_star(lala, randint(-300, 300), randint(0, 300), 15)
        i += 1

# Drawing the buildings.
    i: int = -5
    while i < 3:
        draw_rectangle(lala, ((i + 1) * -120) - 150, (i - 50) + 100, 100, 350)
        i += 1
    

    i: int = -5
    while i < 3:
        draw_rectangle(lala, ((i + 1) * -120), (i - 50), 100, 350)
        i += 1
    

# Drawing windows on buildings randomly.
    i: int = 0
    lala.color(255, 226, 49)
    while i < 10:
        draw_square(lala, randint(-300, 300), randint(-300, 0), 12)
        i += 1
    
    i: int = 0
    lala.color(90, 90, 90)
    while i < 10:
        draw_square(lala, randint(-300, 300), randint(-300, 0), 12)
        i += 1


# Draw crescent moon.
    lala.color(243, 196, 87)
    draw_circle(lala, 200, 150, 50)

    lala.color(37, 35, 128)
    draw_circle(lala, 215, 165, 45)

    update()
    done()

# Description of all functions.

def set_up(setup: Turtle, x: float, y: float) -> None:
    """Sets up moving pen before drawing"""
    setup.penup()
    setup.goto(x, y)
    setup.setheading(0.0)
    setup.pendown()


def draw_rectangle(rectangle: Turtle, x: float, y: float, width: float, length: float) -> None:
    """Draw a rectangle of given width/length whose top-left corner is at x, y."""
    
    rectangle.pensize(3)
    rectangle.pencolor(90, 90, 90)
    rectangle.fillcolor(0, 0, 0)
    set_up(rectangle, x, y)

    rectangle.begin_fill()

    i: int = 0
    while i < 4:
        rectangle.forward(width)
        rectangle.right(90)
        rectangle.forward(length)
        rectangle.right(90)
        i = i + 1
    
    rectangle.end_fill()

def draw_star(star: Turtle, x: float, y: float, side_length: float) -> None:
    """Draw a star at given coordinates given length of sides."""

    star.color(255, 226, 49)
    star.penup()
    star.goto(x, y)
    star.setheading(0.0)
    star.pendown()

    star.begin_fill()
    
    for idx in range(0,6):
        star.forward(side_length)
        star.right(144)
    
    star.end_fill()

def draw_square(square: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of the given width whose top-left corner is located at x, y."""
    
    square.penup()
    square.goto(x, y)
    square.setheading(0.0)
    square.pendown()

    square.begin_fill()

    i: int = 0
    while i < 4:
        square.forward(width)
        square.right(90)
        i += 1

    square.end_fill()

def draw_circle(circle: Turtle, x: float, y: float, radius: float) -> None:
    """Draw a circle with given radius and coords."""
    circle.penup()
    circle.goto(x, y)
    circle.setheading(0.0)
    circle.pendown()

    circle.begin_fill()
    circle.circle(radius)
    circle.end_fill()


if __name__ == "__main__":
    main()