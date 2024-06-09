from lib.graphics import Window, Point, Line


def main():
    win = Window(800, 600)
    point1 = Point(10, 10)
    point2 = Point(50, 50)
    line = Line(point1, point2)
    win.draw_line(line, "red")
    win.wait_for_close()


main()
