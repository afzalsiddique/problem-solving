from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def findPairs(self, A: List[int], k: int) -> int:
        if k==0:
            count=Counter(A)
            return sum(1 for x in count if count[x]>1)
        sett=set()
        res=0
        for x in A:
            if x in sett: continue
            if x-k in sett:
                res+=1
            if x+k in sett:
                res+=1
            sett.add(x)
        return res
class Solution2:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        minn = nums[-1] - k
        cnt = 0
        for i in range(len(nums)):
            if nums[i] > minn:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            key = nums[i] + k
            idx = bisect_right(nums, key)
            idx -= 1
            if idx >= 0 and nums[idx] == key and idx!=i:
                cnt += 1
        return cnt

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(2, get_sol().findPairs( [3,1,4,1,5],  2))
    def test02(self):
        self.assertEqual(4, get_sol().findPairs( [1,2,3,4,5],  1))
    def test03(self):
        self.assertEqual(1, get_sol().findPairs( [1,3,1,5,4],  0))
    def test04(self):
        self.assertEqual(2, get_sol().findPairs( [1,2,4,4,3,3,0,9,2,3],  3))
    def test06(self):
        self.assertEqual(2, get_sol().findPairs( [-1,-2,-3],  1))
