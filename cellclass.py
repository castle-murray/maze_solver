from pointclass import Point
from lineclass import Line
class Cell():
    def __init__(self, x1, y1, x2, y2, window):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = window
        self.visited = False
    

    def draw(self):
        point1 = Point(self._x1, self._y1)
        point2 = Point(self._x2, self._y1)
        point3 = Point(self._x2, self._y2)
        point4 = Point(self._x1, self._y2)

        if self.has_left_wall:
            line1 = Line(point1, point4)
            self._win.draw_line(line1, "black")
        else:
            line1 = Line(point1, point4)
            self._win.draw_line(line1, "white")
        if self.has_right_wall:
            line2 = Line(point2, point3)
            self._win.draw_line(line2, "black")
        else:
            line2 = Line(point2, point3)
            self._win.draw_line(line2, "white")
        if self.has_top_wall:
            line3 = Line(point1, point2)
            self._win.draw_line(line3, "black")
        else:
            line3 = Line(point1, point2)
            self._win.draw_line(line3, "white")
        if self.has_bottom_wall:
            line4 = Line(point3, point4)
            self._win.draw_line(line4, "black")
        else:
            line4 = Line(point3, point4)
            self._win.draw_line(line4, "white")
    
    def get_path_point(self):
        offset = self._x2//2 - self._x1//2
        return Point(self._x1 + offset, self._y1 + offset)

    def draw_move(self, to_cell, undo=False):
        if undo:
            color = "gray"
        else:
            color = "red"
        point1 = self.get_path_point()
        point2 = to_cell.get_path_point()
        line = Line(point1, point2)
        self._win.draw_line(line, color)

    def break_wall(self, wall):
        if wall == 'left':
            self.has_left_wall = False
        elif wall == 'right':
            self.has_right_wall = False
        elif wall == 'top':
            self.has_top_wall = False
        elif wall == 'bottom':
            self.has_bottom_wall = False
