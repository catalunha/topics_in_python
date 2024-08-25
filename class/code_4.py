from dataclasses import dataclass

"""
Python automatically creates methods like __init__(), __repr__(), and __eq__() based on the class attributes you define.
"""


@dataclass
class Point:
    x: int
    y: int


point = Point(2, 3)
print(point)  # Output: Point(x=2, y=3)
