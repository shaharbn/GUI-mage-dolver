from point import *

class Line():
    """
    this class represent a drawblw line
    point1 represent a point object
    point2 represent another point object

    methods:
    draw(canvas, color)
        draw a straight useing point1 and point2
    """
    def __init__(self, point1, point2):
        """
        point1 represent a point object
        point2 represent another point object
        """
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, color):
        """
        params:
        canvas - canvas from window class
        color - string that represent color like 'red'
        """
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=color, width=2
        )