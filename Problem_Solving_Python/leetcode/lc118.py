from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
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
    def test01(self):
        self.assertEqual([[1]],get_sol().generate(1))
    def test02(self):
        e = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
        self.assertEqual(e, get_sol().generate(5))
