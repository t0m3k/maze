from lib.graphics import Window, Point, Cell


def main():
    win = Window(800, 600)
    point1 = Point(10, 10)
    cell = Cell(point1, win)
    cell.draw()
    win.wait_for_close()


main()
