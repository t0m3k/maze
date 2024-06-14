import math
import random
from lib.cell import Cell
from lib.graphics import Window, Point
from time import sleep


class Maze:
    def __init__(
        self,
        point: Point,
        num_rows,
        num_cols,
        cell_size,
        win: Window,
    ):
        self.__position = point
        self.rows = num_rows
        self.cols = num_cols
        Cell.size = cell_size
        self.__win = win
        self._cells: list[Cell] = []
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        pos = self.__position
        for i in range(self.cols * self.rows):
            cell = Cell(pos, self.__win)
            self._cells.append(cell)
            cell.draw()
            self._animate()
            if (i + 1) % self.cols == 0 and i is not 0:
                x = self.__position.x
                y = cell.get_bottom_left().y
                pos = Point(x, y)
            else:
                pos = cell.get_top_right()

    def _break_entrance_and_exit(self):
        self._cells[0].has_top_wall = False
        self._animate()
        self._cells[0].draw()
        self._cells[-1].has_bottom_wall = False
        self._cells[-1].draw()
        self._animate()

    def _animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        sleep(0.01)

    def get_neighbors(self, i: int, all=True) -> list[int]:
        nbrs: list[int] = []
        if i + 1 > self.cols and (all or not self._cells[i].has_top_wall):
            nbr = i - self.cols
            if all or not self._cells[nbr].has_bottom_wall:
                nbrs.append(nbr)

        if i < (self.cols * self.rows) - self.cols and (
            all or not self._cells[i].has_bottom_wall
        ):
            nbr = i + self.cols
            if all or not self._cells[nbr].has_top_wall:
                nbrs.append(nbr)

        if i % self.cols > 0 and (all or not self._cells[i].has_left_wall):
            nbr = i - 1
            if all or not self._cells[nbr].has_right_wall:
                nbrs.append(nbr)

        if i % self.cols is not self.cols - 1 and (
            all or not self._cells[i].has_right_wall
        ):
            nbr = i + 1
            if all or not self._cells[nbr].has_left_wall:
                nbrs.append(nbr)

        return nbrs

    def break_walls_r(self, cell: int):
        if cell == len(self._cells) - 1:
            if self.__visited_ratio() > 0.99:
                return
        self._cells[cell].visited = True
        nbrs = list(
            filter(lambda i: not self._cells[i].visited, self.get_neighbors(cell))
        )
        if not nbrs:
            if self._cells[-1].visited and self.__visited_ratio() > 0.99:
                return
            return self.break_walls_r(self.__random_not_visited())
        n2 = random.choice(nbrs)
        self.remove_common_wall(cell, n2)
        self.break_walls_r(n2)

    def __clear_visited(self):
        for cell in self._cells:
            cell.visited = False

    def __visited_ratio(self):
        if not self._cells:
            return 1
        visited = 0
        for cell in self._cells:
            if cell.visited:
                visited += 1
        return visited / len(self._cells)

    def __random_not_visited(self) -> list[Cell]:
        nv: list[Cell] = []
        for i in range(len(self._cells)):
            if not self._cells[i].visited:
                nbrs = self.get_neighbors(i)
                nbrs = list(filter(lambda n: self._cells[n].visited, nbrs))
                nv += nbrs
        if not nv:
            return
        return random.choice(nv)

    def remove_common_wall(self, n1, n2):
        if n1 + 1 == n2:
            self._cells[n1].has_right_wall = False
            self._cells[n2].has_left_wall = False

        if n1 - 1 == n2:
            self._cells[n1].has_left_wall = False
            self._cells[n2].has_right_wall = False

        if n1 + self.cols == n2:
            self._cells[n1].has_bottom_wall = False
            self._cells[n2].has_top_wall = False

        if n1 - self.cols == n2:
            self._cells[n1].has_top_wall = False
            self._cells[n2].has_bottom_wall = False

        self._cells[n1].draw()
        self._cells[n2].draw()
        self._animate()

    def solve(self):
        self.__clear_visited()
        return self.__solve_r(0)

    def __solve_r(self, i):
        self._animate()
        if i == len(self._cells) - 1:
            return True
        c_cell = self._cells[i]
        c_cell.visited = True
        nbrs = self.get_neighbors(i, False)
        for nbr in nbrs:
            n_cell = self._cells[nbr]
            if not n_cell.visited:
                c_cell.draw_move(n_cell)
                if self.__solve_r(nbr):
                    return True
                c_cell.draw_move(n_cell, True)
