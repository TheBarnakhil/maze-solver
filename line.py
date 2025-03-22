from tkinter import Canvas

class Point:
    def __init__(self,x ,y) -> None:
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1: Point, p2 : Point) -> None:
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas: Canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, width=2)
    
    