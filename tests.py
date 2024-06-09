import unittest
from lib.maze import Maze
from lib.graphics import Point


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(Point(0, 0), num_rows, num_cols, 10, None)
        self.assertEqual(
            len(m1._cells),
            num_cols * num_rows,
        )


if __name__ == "__main__":
    unittest.main()
