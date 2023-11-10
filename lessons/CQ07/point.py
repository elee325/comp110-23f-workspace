"""Creating and comparing two methods - one that mutates, one that doesn't."""

from __future__ import annotations


class Point:
    """Creating new class, Point."""
    # representation of a point on a coordinate graph
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """My constructor."""
        self.x = x_init
        self.y = y_init

    # mutating method
    def scale_by(self, factor: int):
        """Updates x and y attributes by multiplying x and y by factor."""
        self.x *= factor
        self.y *= factor

    # instead of mutating, creates a new point
    def scale(self, factor: int) -> Point:
        """Creating new point after multiplying by factor."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    # str magic method that prints out points in readable way
    def __str__(self) -> str:
        """Magic Method that prints out points in readable way."""
        output: str = f"x: {self.x}; y: {self.y}"
        return output
    
    def __mul__(self, factor: int | float) -> Point:
        """Creates new Point where x and y are multiplied by factor."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __add__(self, factor: int | float) -> Point:
        """Overloads addition by adding factor to x and y."""
        new_point: Point = Point(self.x + factor, self.y + factor)
        return new_point


my_point: Point = Point()
print(my_point)
