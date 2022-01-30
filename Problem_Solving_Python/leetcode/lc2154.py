from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        def getSum(i,j):
            return pre[j+1]-pre[i]
        n=len(nums)
        res=[]
        pre=list(accumulate(nums))
        pre=[0]+pre
        for i in range(n):
            zeros=(i)-getSum(0,i-1)
            ones=getSum(i,n-1)
            res.append(zeros+ones)
        res.append(n-pre[-1])
        maxx=max(res)
        return [i for i in range(n+1) if res[i]==maxx]

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual([2,4], get_sol().maxScoreIndices([0,0,1,0]))
    def test02(self):
        self.assertEqual([3], get_sol().maxScoreIndices([0,0,0]))
    def test03(self):
        self.assertEqual([0], get_sol().maxScoreIndices([1,1]))
    def test04(self):
        self.assertEqual([0], get_sol().maxScoreIndices([1]))
    def test05(self):
        self.assertEqual([1], get_sol().maxScoreIndices([0]))
