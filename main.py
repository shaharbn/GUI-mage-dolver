from window import *
from point import *
from line import *

def main():
    win = Window(800, 600)

    point1 = Point(0, 0)
    point2 = Point(800,600)
    line1 = Line(point1, point2)
    win.draw_line(line1, "black")

    win.wait_for_close()

if __name__ == "__main__":
    main()