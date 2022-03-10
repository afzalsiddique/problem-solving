from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=khddrw6Bfyw
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort()
        n = len(people)
        res = [[-1,None] for _ in range(n)]
        for my_h,my_f in people:
            cnt = my_f
            for i in range(n):
                h = res[i][0]
                if not cnt and h==-1:
                    res[i] = [my_h,my_f]
                    break
                if h>=my_h or h==-1:
                    cnt-=1
        return res

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual([[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]],get_sol().reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
    def test02(self):
        self.assertEqual([[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]],get_sol().reconstructQueue([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]))
