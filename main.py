from window import *
from maze import *
def main():
    win = Window(800, 600)

    maze = Maze(5,5,5,5,30,30,win)

    win.wait_for_close()

if __name__ == "__main__":
    main()