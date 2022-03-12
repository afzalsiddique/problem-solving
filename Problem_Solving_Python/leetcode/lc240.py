from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n-1
        while row<m and col >=0:
            if target==matrix[row][col]:
                return True
            if target < matrix[row][col]:
                col-=1
            else:
                row+=1
        return False

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(False, get_sol().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],  20))
    def test02(self):
        self.assertEqual(True, get_sol().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],  5))