class Line():
    def __init__(self, pointa, pointb):
        self.pt_a = pointa
        self.pt_b = pointb

    def draw(self,canvas,fill_color):
        canvas.create_line(self.pt_a.x, self.pt_a.y, self.pt_b.x, self.pt_b.y, fill=fill_color ,width=2)
