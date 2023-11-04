"""Creating and comparing two methods - one that mutates, one that doesn't."""

from __future__ import annotations


class Point:
    """Creating new class, Point."""
    # representation of a point on a coordinate graph
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
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
