import unittest
from collections import deque
from typing import List

from typing import List

class Solution:
    # https://leetcode.com/problems/prison-cells-after-n-days/discuss/717491/Python-Loop-detection-explained
    def next_step(self, cells):
        res = [0] * 8
        for i in range(1,7):
            res[i] = int(cells[i-1] == cells[i+1])
        return res

    def prisonAfterNDays(self, cells, N):
        found_dic = {}
        for i in range(N):
            cells_str = str(cells)
            if cells_str in found_dic:
                loop_len = i - found_dic[cells_str]
                # N - i loops is because i is the start of the loop. For example, consider [a b c d e c d e c d e].
                # The loop starts at element ''c' which is at i ( the starting of the loop ) and (N - i) removes the
                # elements that are not a part of the loop. The previous elements which are a,b,c,d,e are removed and
                # we have to search only within the loop [c d e c d e]
                # The given original array may be or may not be part of the loop
                return self.prisonAfterNDays(cells, (N - i) % loop_len)
            else:
                found_dic[cells_str] = i
                cells = self.next_step(cells)

        return cells


def get_sol_obj():
    return Solution()

class tester(unittest.TestCase):
    def test1(self):
        cells = [0,1,0,1,1,0,0,1]
        n = 1
        Output= [0, 1, 1, 0, 0, 0, 0, 0]
        self.assertEqual(Output,get_sol_obj().prisonAfterNDays(cells,n))
    def test2(self):
        cells = [0,1,0,1,1,0,0,1]
        n = 7
        Output=  [0,0,1,1,0,0,0,0]
        self.assertEqual(Output,get_sol_obj().prisonAfterNDays(cells,n))
    def test3(self):
        cells = [1,0,0,1,0,0,1,0]
        n = 1000000000
        Output= [0,0,1,1,1,1,1,0]
        self.assertEqual(Output,get_sol_obj().prisonAfterNDays(cells,n))