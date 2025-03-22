from cell import Cell
from graphics import Window
from line import Line, Point

import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win : Window = None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        self._matrix_maze = [ [Cell(self._win) for j in range(self._num_rows)] for x in range(self._num_cols)]
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
            x1 = self._x1 + i * self._cell_size_x
            y1 = self._y1 + j * self._cell_size_y
            x2 = x1 + self._cell_size_x
            y2 = y1 + self._cell_size_y
            cornerA = Point(x1, y1)
            cornerB = Point(x2, y2)
            if self._win:
                self._matrix_maze[i][j].draw(cornerA, cornerB)
                self._animate()
    
    def _animate(self):
         self._win.redraw()
         time.sleep(0.05)

    def _break_entrance_and_exit(self):
         self._matrix_maze[0][0].has_top_wall = False
         self._matrix_maze[self._num_cols -1][self._num_rows -1].has_bottom_wall = False
         self._draw_cell(0,0)
         self._draw_cell(self._num_cols -1, self._num_rows -1)