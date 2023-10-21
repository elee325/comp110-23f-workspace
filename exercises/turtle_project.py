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
    idx: int = -5
    while idx < 3:
        draw_rectangle(lala, ((idx + 1) * -120) - 150, (idx - 50) + 100, 100, 350)
        idx += 1
    

    idx1: int = -5
    while idx1 < 3:
        draw_rectangle(lala, ((idx1 + 1) * -120), (idx1 - 50), 100, 350)
        idx1 += 1
    

# Drawing windows on buildings randomly.
    idx2: int = 0
    lala.color(255, 226, 49)
    while idx2 < 10:
        draw_square(lala, randint(-300, 300), randint(-300, 0), 12)
        idx2 += 1
    
    idx3: int = 0
    lala.color(90, 90, 90)
    while idx3 < 10:
        draw_square(lala, randint(-300, 300), randint(-300, 0), 12)
        idx3 += 1


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
    set_up(star, x, y)


    star.begin_fill()
    
    for idx in range(0,6):
        star.forward(side_length)
        star.right(144)
    
    star.end_fill()

def draw_square(square: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of the given width whose top-left corner is located at x, y."""
    
    set_up(square, x, y)


    square.begin_fill()

    i: int = 0
    while i < 4:
        square.forward(width)
        square.right(90)
        i += 1

    square.end_fill()

def draw_circle(circle: Turtle, x: float, y: float, radius: float) -> None:
    """Draw a circle with given radius and coords."""
    set_up(circle, x, y)


    circle.begin_fill()
    circle.circle(radius)
    circle.end_fill()


if __name__ == "__main__":
    main()