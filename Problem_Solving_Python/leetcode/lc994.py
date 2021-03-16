# https://leetcode.com/problems/rotting-oranges/discuss/563686/Python-Clean-and-Well-Explained-(faster-than-greater-90)
# https://www.youtube.com/watch?v=CxrnOTUlNJE
import math
import unittest
from collections import deque
from typing import List


# without destroying the input
class Solution:

    def get_grid_state(self, grid):

        fresh, rotten = set(), set()
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                pos = (row,col)
                if grid[row][col] == 2:
                    rotten.add(pos)
                elif grid[row][col] == 1:
                    fresh.add(pos)

        return fresh, rotten

    def orangesRotting(self, grid: List[List[int]]) -> int:
        # get (row,col) for fresh and rotten oranges (as a set)
        fresh, rotten = self.get_grid_state(grid)

        # convert rotten set to list for adding it to queue
        q = deque(list(rotten))
        mins_to_rotten = 0

        # peform BFS while we have rotten oranges and fresh oranges
        while q and fresh:
            mins_to_rotten += 1

            # iterate rotten oranges at this level only
            for _ in range(len(q)):
                rotten_row, rotten_col = q.popleft()

                # iterate thru neighboring grids
                for delta_row, delta_col in [(1,0), (-1,0), (0,1), (0,-1)]:
                    next_pos = (rotten_row+delta_row, rotten_col+delta_col)
                    if next_pos in fresh:
                        # next_pos has a fresh orange. NOTE: we don't have to worry about out of bounds check since fresh will only contain valid cell positions
                        q.append(next_pos)
                        # add fresh orange to the q and remove it from the fresh set
                        # ensures a loop free BFS traversal without explicity taking care of visited positions
                        fresh.remove(next_pos)

        return -1 if len(fresh) != 0 else mins_to_rotten

class MyTestCase(unittest.TestCase):
    def test_1(self):
        grid = [[2,1,1],[1,1,0],[0,1,1]]
        actual = Solution().orangesRotting(grid)
        expected = 4
        self.assertEqual(expected,actual)
    def test_2(self):
        grid = [[2,1,1],[0,1,1],[1,0,1]]
        actual = Solution().orangesRotting(grid)
        expected = -1
        self.assertEqual(expected,actual)
    def test_3(self):
        grid = [[0,2]]
        actual = Solution().orangesRotting(grid)
        expected = 0
        self.assertEqual(expected,actual)
    def test_4(self):
        grid = [[2,2],[1,1],[0,0],[2,0]]
        actual = Solution().orangesRotting(grid)
        expected = 1
        self.assertEqual(expected,actual)
