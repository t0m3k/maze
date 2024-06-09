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
        sleep(0.05)
