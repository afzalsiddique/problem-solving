from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        def helper(row):
            n = len(row)
            new_row= []
            for i in range(n-2+1):
                new_row.append(row[i]+row[i+1])
            return [1] + new_row + [1]

        ans = [[1]]
        result = [[1]]
        for _ in range(numRows-1):
            ans = helper(ans)
            result.append(ans)
        return result


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual([[1]],Solution().generate(1))
    def test_2(self):
        e = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
        self.assertEqual(e, Solution().generate(5))