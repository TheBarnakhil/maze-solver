from line import Point, Line
from graphics import Window
from tkinter import Canvas

class Cell:
    def __init__(self, win : Window, ) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self.__win = win
    
    def draw(self, p1: Point, p2: Point):
        self.__x1 = p1.x
        self.__x2 = p2.x
        self.__y1 = p1.y
        self.__y2 = p2.y
        if self.has_left_wall:
            left_line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(left_line, "black")
        if self.has_right_wall:
            right_line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(right_line, "black")
        if self.has_top_wall:
            top_line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(top_line, "black")
        if self.has_bottom_wall:
            bottom_line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(bottom_line, "black")