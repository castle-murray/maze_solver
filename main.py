#python3.13
from windowclass import Window
from maze import Maze
import sys
sys.setrecursionlimit(10000)

    
def main():
    start_x = 15
    start_y = 15
    width = 1400
    height = 1400
    num_cols = 50
    num_rows = 50
    cell_size_x = (width - start_x*2 ) // num_cols
    cell_size_y = (height - start_y*2 ) // num_rows
    window = Window(width, height)
    maze = Maze(start_x, start_y, num_rows, num_cols, cell_size_x, cell_size_y, window)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0,0)
    maze._reset_visited()
    maze._solve_maze(0,0)


    window.wait_for_close()

if __name__ == "__main__":
    main()
