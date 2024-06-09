from lib.graphics import Window, Point
from lib.maze import Maze


def main():
    win = Window(800, 600)
    point = Point(10, 10)
    maze = Maze(point, 1, 10, 50, win)

    win.wait_for_close()


main()
