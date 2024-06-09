from lib.graphics import Window, Point, Cell


def main():
    win = Window(800, 600)
    point1 = Point(10, 10)
    cell1 = Cell(point1, win)
    cell1.has_right_wall = False
    cell2 = Cell(cell1.get_top_right(), win)
    cell2.has_left_wall = False
    cell1.draw()
    cell2.draw()

    cell1.draw_move(cell2)

    win.wait_for_close()


main()
