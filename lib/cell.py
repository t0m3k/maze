from lib.graphics import Line, Point, Window


class Cell:
    size = 50

    def __init__(self, position: Point, win: Window) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.position = position
        self.__win = win

    def draw(self) -> None:
        if self.__win is None:
            return None
        if self.has_top_wall:
            line = Line(self.position, self.get_top_right())
            self.__win.draw_line(line, "red")
        if self.has_left_wall:
            line = Line(self.position, self.get_bottom_left())
            self.__win.draw_line(line, "red")
        if self.has_bottom_wall:
            line = Line(self.get_bottom_right(), self.get_bottom_left())
            self.__win.draw_line(line, "red")
        if self.has_right_wall:
            line = Line(self.get_top_right(), self.get_bottom_right())
            self.__win.draw_line(line, "red")

    def draw_move(self, to_cell: "Cell", undo=False) -> None:
        line = Line(self.__center(), to_cell.__center())
        colour = "gray" if undo else "red"
        self.__win.draw_line(line, colour)

    def __center(self) -> Point:
        return Point(self.position.x + self.size / 2, self.position.y + self.size / 2)

    def get_top_right(self) -> Point:
        return Point(self.position.x + self.size, self.position.y)

    def get_bottom_right(self) -> Point:
        return Point(self.position.x + self.size, self.position.y + self.size)

    def get_bottom_left(self) -> Point:
        return Point(self.position.x, self.position.y + self.size)
