from tkinter import Tk, BOTH, Canvas


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end

    def draw(self, canvas: Canvas, fill_color: str) -> None:
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2
        )


class Window:
    def __init__(self, w, h) -> None:
        self.__root = Tk()
        self.__root.title = "Tomasz test"
        self.__canvas = Canvas(self.__root, width=w, height=h)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, line: Line, fill_color: str) -> None:
        line.draw(self.__canvas, fill_color)

    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False


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
