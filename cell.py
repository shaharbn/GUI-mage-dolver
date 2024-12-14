from line import *
from point import *
from window import *
class Cell():
    """
    this class represent cells in the maze and draw the cells in the maze
    """
    def __init__(self, win):
        """
        xi, yi - int that represent xi and yi in 2d graphs
        win - the canvas window
        """
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        """
        draw a cell in the canvas
        """
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        point1 = Point(self.__x1, self.__y1)
        point2 = Point(self.__x2, self.__y1)
        point3 = Point(self.__x2, self.__y2)
        point4 = Point(self.__x1, self.__y2)
        if self.has_left_wall:
            left_wall = Line(point1, point4)
            self._win.draw_line(left_wall, "black")
        if self.has_right_wall:
            right_wall = Line(point2, point3)
            self._win.draw_line(right_wall, "black")
        if self.has_top_wall:
            top_wall = Line(point1, point2)
            self._win.draw_line(top_wall, "black")
        if self.has_bottom_wall:
            bottom_wall = Line(point4, point3)
            self._win.draw_line(bottom_wall, "black")

    def draw_move(self, to_cell, undo=False):
        """
        draw a move between 2 cells
        """
        x1 = (self.__x1 + self.__x2) // 2
        y1 = (self.__y1 + self.__y2) // 2
        x2 = (to_cell.__x1 + to_cell.__x2) // 2
        y2 = (to_cell.__y1 + to_cell.__y2) // 2

        point1 = Point(x1, y1)
        point2 = Point(x2, y2)
        line = Line(point1, point2)

        if undo:
            self._win.draw_line(line, "gray")
        else:
            self._win.draw_line(line, "red")