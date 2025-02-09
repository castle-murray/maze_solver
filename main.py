#python3.13
from window import Window
from point import Point
from line import Line
    
def main():
    window = Window()
    window.wait_for_close()

    point1 = Point(1,1)
    point2 = Point(20, 20)
    line = Line(point1, point2)
    window.draw_line(line, "black")


if __name__ == "__main__":
    main()

