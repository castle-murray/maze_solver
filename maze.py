from cellclass import Cell
from time import sleep
import random

ANIMATION_SPEED = 0.001

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
            ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = self._create_cells()

    
    def _create_cells(self):
        cell_graph = []
        cx1 = self.x1
        cy1 = self.y1
        for _ in range(0,self.num_rows):
            row = []
            for _ in range(0,self.num_cols):
                cell = Cell(
                        cx1,
                        cy1,
                        cx1+self.cell_size_x,
                        cy1+self.cell_size_y,
                        self.win,)
                row.append(cell)
                cx1 += self.cell_size_x
            cell_graph.append(row)
            cx1 = self.x1
            cy1 += self.cell_size_y
        for row in cell_graph:
            for cell in row:
                self._draw_cells(cell)
        return cell_graph
        
    def _draw_cells(self, cell):
        cell.draw()
        self._animate()
                
    def _animate(self):
        self.win.redraw()
        sleep(ANIMATION_SPEED)

    def _break_entrance_and_exit(self):
        self._cells[0][0].break_wall('top')
        self._draw_cells(self._cells[0][0])
        self._cells[self.num_rows-1][self.num_cols-1].break_wall('bottom')
        self._draw_cells(self._cells[self.num_rows-1][self.num_cols-1])
        
    def _break_walls_r(self,i,j):
        to_visit = []
        current_cell = self._cells[i][j]
        self._cells[i][j].visited = True
        if i == self.num_rows or i < 0 or j == self.num_cols or j < 0:
            return

        if i+1 != self.num_rows:
            if not self._cells[i+1][j].visited:
                to_visit.append((i+1,j))
        if not i-1 < 0: 
            if not self._cells[i-1][j].visited:
                to_visit.append((i-1,j))
        if j+1 != self.num_cols:
            if not self._cells[i][j+1].visited:
                to_visit.append((i,j+1))
        if not j-1 < 0:
            if not self._cells[i][j-1].visited:
                to_visit.append((i,j-1))

        if len(to_visit) == 0:
            return
        if len(to_visit) >= 1:
            while len(to_visit) != 0:
                random_index = random.randint(0,len(to_visit)-1)
                picked = to_visit[random_index]
                to_visit.pop(random_index)
                temp_i = picked[0]
                temp_j = picked[1]
                if self._cells[temp_i][temp_j].visited:
                    continue

                if temp_i > i:
                    current_cell.has_bottom_wall = False
                    current_cell.break_wall('bottom')
                    self._cells[temp_i][temp_j].has_top_wall = False
                elif temp_i < i: 
                    current_cell.has_top_wall = False
                    current_cell.break_wall('top')
                    self._cells[temp_i][temp_j].has_bottom_wall = False
                elif temp_j > j:
                    current_cell.has_right_wall = False
                    current_cell.break_wall('right')
                    self._cells[temp_i][temp_j].has_left_wall = False
                elif temp_j < j:
                    current_cell.has_left_wall = False
                    current_cell.break_wall('left')
                    self._cells[temp_i][temp_j].has_right_wall = False
                current_cell.draw()
                self._animate()

                self._break_walls_r(temp_i,temp_j)

    def _reset_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False
    
    def _solve_maze(self,i,j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True
        if i == self.num_rows -1 and j == self.num_cols -1:
            return 1
        to_visit = []
        if i != 0:
            if not current_cell.has_top_wall:
                if not self._cells[i-1][j].visited:
                    to_visit.append((i-1,j))
        if j != self.num_cols -1:
            if not current_cell.has_right_wall:
                if not self._cells[i][j+1].visited:
                    to_visit.append((i,j+1))
        if i != self.num_rows -1:
            if not current_cell.has_bottom_wall:
                if not self._cells[i+1][j].visited:
                    to_visit.append((i+1,j))
        if j != 0:
            if not current_cell.has_left_wall:
                if not self._cells[i][j-1].visited:
                    to_visit.append((i,j-1))

        if len(to_visit) == 0:
            return 0
        result = 0
        for picked in to_visit:
            temp_i = picked[0]
            temp_j = picked[1]
            next_cell = self._cells[temp_i][temp_j]
            current_cell.draw_move(next_cell)
            result = self._solve_maze(temp_i,temp_j)
            if result == 0:
                current_cell.draw_move(next_cell,True)
            else:
                return result
        return result


