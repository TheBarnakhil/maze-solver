from line import Point, Line
from graphics import Window
from tkinter import Canvas

class Cell:
    def __init__(self, win : Window = None ) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False
    
    def draw(self, p1: Point, p2: Point):
        self._x1 = p1.x
        self._x2 = p2.x
        self._y1 = p1.y
        self._y2 = p2.y
        left_line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        right_line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        top_line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        bottom_line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        if self.has_left_wall:
            self._win.draw_line(left_line, "black")
        else:
            self._win.draw_line(left_line, "white")
        if self.has_right_wall:
            self._win.draw_line(right_line, "black")
        else:
            self._win.draw_line(right_line, "white")
        if self.has_top_wall:
            self._win.draw_line(top_line, "black")
        else:
            self._win.draw_line(top_line, "white")
        if self.has_bottom_wall:
            self._win.draw_line(bottom_line, "black")
        else:
            self._win.draw_line(bottom_line, "white")
    
    def compute_center(self) -> Point:
        half_length_x = abs(self._x1 - self._x2) // 2
        half_length_y = abs(self._y1 - self._y2) // 2
        return Point(half_length_x+self._x1, half_length_y + self._y1)

    def draw_move(self, to_cell, undo=False):
        fill_color = "red" if not undo else "gray"
        centerA = self.compute_center()
        centerB = to_cell.compute_center()
        self._win.draw_line(Line(centerA, centerB), fill_color)
