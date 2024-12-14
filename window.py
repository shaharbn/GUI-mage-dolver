from tkinter import Tk, BOTH, Canvas
from line import *

class Window():
    """
    The class represent a empty graphical window to draw on.

    Attributes:
    private
    -------
    root : Tk widget
        represnt the graphical window object for tkinter
    title : Tk method
        represnt the gui canvas to drow on
    canvas
        canvas
    is_running : boolean
        represent if window is running

    public
    ------

    Methods:
        redraw()
            update all the graphics in the window
        wait_for_close()
            use redraw method over and over to update the graphics
        close()
            close the program
        draw_line(line, color)
            draw a line on the canvas
    """
    def __init__(self, width, height):
        """
        Parameters:
        width : int
            represent the width of the window
        height : int
            represent the height of the window
        """
        self.__root = Tk()
        self.__title = self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        """
        redrew all the graphics in the window
        """
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        """
        use redraw method over and over to update the graphics
        """
        self.__running = True
        while self.__running:
            self.redraw()
        print("windows closed...")

    def close(self):
        """
        close the program
        """
        self.__running = False

    def draw_line(self, line, color):
        """
        line - line instance
        color - string of color
        """
        line.draw(self.__canvas, color)