from graphics import Window
from line import Line, Point
from cell import Cell

def main():
    win = Window(800,600)
    p1 = Point(10, 10)
    p2 = Point(210, 210)
    pA = Point(220, 10)
    pB = Point(420, 210)
    cell1 = Cell(win)
    cell2 = Cell(win)
    cell1.draw(p1, p2)
    cell2.draw(pA, pB)
    win.wait_for_close()

main()
    