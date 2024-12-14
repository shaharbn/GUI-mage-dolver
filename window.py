from tkinter import Tk, BOTH, Canvas

class Window():
    """
    The class represent a empty graphical window to draw on.

    Attributes:
    root : Tk widget
        represnt the graphical window object for tkinter
    title : Tk method
        represnt the gui canvas to drow on
    is_running : boolean
        represent if window is running

    Methods:
        redraw()
            update all the graphics in the window
        wait_for_close()
            use redraw method over and over to update the graphics
        close()
            close the program
    """
    def __init__(self, width, height):
        """
        Parameters:
        width : int
            represent the width of the window
        height : int
            represent the height of the window
        """
        self.root = Tk()
        self.title = self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        """
        redrew all the graphics in the window
        """
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        """
        use redraw method over and over to update the graphics
        """
        self.running = True
        while self.running:
            self.redraw()
        print("windows closed...")

    def close(self):
        """
        close the program
        """
        self.running = False