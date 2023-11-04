"""Checking Methods for Correctness."""

from lessons.CQ07.point import Point

my_point: Point = Point(2, 2)

my_point.scale_by(2)
print(my_point.x, my_point.y)