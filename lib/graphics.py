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
            line = Line(self.position, self.__tr())
            self.__win.draw_line(line, "red")
        if self.has_left_wall:
            line = Line(self.position, self.__bl())
            self.__win.draw_line(line, "red")
        if self.has_bottom_wall:
            line = Line(self.__br(), self.__bl())
            self.__win.draw_line(line, "red")
        if self.has_left_wall:
            line = Line(self.__tr(), self.__br())
            self.__win.draw_line(line, "red")

    def __tr(self) -> Point:
        return Point(self.position.x + self.size, self.position.y)

    def __br(self) -> Point:
        return Point(self.position.x + self.size, self.position.y + self.size)

    def __bl(self) -> Point:
        return Point(self.position.x, self.position.y + self.size)
