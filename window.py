from tkinter import Tk, Canvas, BOTH
from point import Point, Line

class Window(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.title("Maze Solver")
        self.canvas = Canvas(self, bg="white")
        self.canvas.pack()
        self.running = False

    def redraw(self): 
        self.update_idletasks()
        self.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False
        
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

        
