from tkinter import Tk, BOTH, Canvas

from line import Line

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("window closed...")
    
    def close(self):
        self.running = False
    
    def draw_line(self, line: Line, fill_color="black"):
        line.draw(self.canvas, fill_color)
