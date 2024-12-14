from cell import *
from window import *
import time
import random

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

    def __create_cells(self):
        for i in range(self.__num_cols):
            col = []
            for j in range(self.__num_rows):
                col.append(Cell(self.__win))
            self.__cells.append(col)
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        x1 = self.__x1 + (i * self.__cell_size_x)
        y1 = self.__y1 + (j * self.__cell_size_y)
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        self.__win.redraw()
        time.sleep(0.05)
        
    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            possible_directions = []
            # check top cell
            if j-1 >= 0:
                if not self.__cells[i][j-1].visited:
                    possible_directions.append([i, j-1])
            # check bot cell
            if j+1 < self.__num_rows:
                if not self.__cells[i][j+1].visited:
                    possible_directions.append([i, j+1])
            # check left cell
            if i-1 >= 0:
                if not self.__cells[i-1][j].visited:
                    possible_directions.append([i-1, j])
            # check right cell
            if i+1 < self.__num_cols:
                if not self.__cells[i+1][j].visited:
                    possible_directions.append([i+1, j])

            if len(possible_directions) == 0:
                self.__draw_cell(i, j)
                return
                
            else:
                direction = random.randrange(len(possible_directions))
                next_direction = possible_directions[direction]
                if j-1 == next_direction[1]:
                    self.__cells[i][j].has_top_wall = False
                    self.__draw_cell(i, j)
                    self.__cells[i][j-1].has_bottom_wall = False
                    self.__draw_cell(i, j-1)
                elif j+1 == next_direction[1]:
                    self.__cells[i][j].has_bottom_wall = False
                    self.__draw_cell(i, j)
                    self.__cells[i][j+1].has_top_wall = False
                    self.__draw_cell(i, j+1)
                elif i-1 == next_direction[0]:
                    self.__cells[i][j].has_left_wall = False
                    self.__draw_cell(i, j)
                    self.__cells[i-1][j].has_right_wall = False
                    self.__draw_cell(i-1, j)
                elif i+1 == next_direction[0]:
                    self.__cells[i][j].has_right_wall = False
                    self.__draw_cell(i, j)
                    self.__cells[i+1][j].has_left_wall = False
                    self.__draw_cell(i+1, j)
            self.__break_walls_r(next_direction[0], next_direction[1])

    def __reset_cells_visited(self):
        for col in self.__cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self.__solve_r(0, 0)

    def __solve_r(self, i=0, j=0):
        self.__animate()
        self.__cells[i][j].visited = True
        if i == self.__num_cols - 1 and j == self.__num_rows - 1:
            return True
        directions = [[i, j-1, "up"],[i, j+1, "down"],[i-1, j, "left"], [i+1, j, "right"]]
        for direction in directions:
            if (0 <= direction[0] < self.__num_cols) and (0 <= direction[1] < self.__num_rows):
                if not self.__cells[direction[0]][direction[1]].visited:
                    if direction[2] == "up":
                        if not self.__cells[i][j].has_top_wall and not self.__cells[i][j-1].has_bottom_wall:
                            self.__cells[i][j].draw_move(self.__cells[i][j-1])
                            if self.__solve_r(i, j-1):
                                return True
                            else:
                                self.__cells[i][j].draw_move(self.__cells[i][j-1], True)
                    if direction[2] == "down":
                        if not self.__cells[i][j].has_bottom_wall and not self.__cells[i][j+1].has_top_wall:
                            self.__cells[i][j].draw_move(self.__cells[i][j+1])
                            if self.__solve_r(i, j+1):
                                return True
                            else:
                                self.__cells[i][j].draw_move(self.__cells[i][j+1], True)
                    if direction[2] == "left":
                        if not self.__cells[i][j].has_left_wall and not self.__cells[i-1][j].has_right_wall:
                            self.__cells[i][j].draw_move(self.__cells[i-1][j])
                            if self.__solve_r(i-1, j):
                                return True
                            else:
                                self.__cells[i][j].draw_move(self.__cells[i-1][j], True)
                    if direction[2] == "right":
                        if not self.__cells[i][j].has_right_wall and not self.__cells[i+1][j].has_left_wall:
                            self.__cells[i][j].draw_move(self.__cells[i+1][j])
                            if self.__solve_r(i+1, j):
                                return True
                            else:
                                self.__cells[i][j].draw_move(self.__cells[i+1][j], True)
        return False