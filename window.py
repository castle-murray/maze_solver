from tkinter import Tk, Canvas, BOTH

class Window(Tk):
    def __init__(self,width,height):
        super().__init__()
        self.width = width
        self.height = height
        self.title("Maze_Solver")
        self.canvas = Canvas(self, width=self.width, height=self.height)
        self.canvas.pack(expand=True, fill=BOTH)
        self.running = False
        self.protocol("WM_DELETE_WINDOW", self.close)
    

    def redraw(self):
        self.update()
        self.update_idletasks()
            

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False
