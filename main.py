from lib.graphics import Window, Point
from lib.maze import Maze


def main():
    win = Window(800, 600)
    point = Point(10, 10)
    maze = Maze(point, 20, 20, 20, win)
    maze.break_walls_r(0)
    maze.solve()
    win.wait_for_close()


main()
