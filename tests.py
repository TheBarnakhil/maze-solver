import unittest
import random

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._matrix_maze),
            num_cols,
        )
        self.assertEqual(
            len(m1._matrix_maze[0]),
            num_rows,
        )
    
    def test_entrance_exit_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._matrix_maze[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            m1._matrix_maze[num_cols -1][num_rows -1].has_bottom_wall,
            False,
        )
    
    def test_cells_visited_reset(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._matrix_maze[0][0].visited,
            False
        )
        self.assertEqual(
            m1._matrix_maze[random.randrange(num_cols)][random.randrange(num_rows)].visited,
            False,
        )

if __name__ == "__main__":
    unittest.main()