from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution2()
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        di = {num:1 for num in nums}
        sett = set(nums)
        for num in di:
            prev = num - di[num]
            while prev in sett:
                di[num] += di[prev]
                sett.remove(prev)
                prev = num -di[num]
        return max(di.values())
class Solution2:
    # without using set
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:return 0
        di = defaultdict(int)
        for num in nums:
            di[num] = 1
        for num in nums:
            prev = num - di[num]
            while di[prev] != 0:
                di[num] += di[prev]
                di[prev]=0
                prev = num -di[num]
        return max(di.values())
class Solution3:
    # without using set
    def longestConsecutive(self, A: List[int]) -> int:
        if not A: return 0
        di={a:1 for a in A}
        for x in di:
            while x-di[x] in di and di[x-di[x]]!=0:
                tmp=x-di[x]
                di[x]+=di[x-di[x]]
                di[tmp]=0
        return max(di.values())
class Solution4:
    # another version
    def longestConsecutive(self, nums: List[int]) -> int:
        def check_left(x, di):
            if x not in di:return 0
            prev = x-1
            if prev not in di:
                return di[x]
            if di[prev]==0:
                return di[x]
            ret = check_left(prev, di)
            di[x] = di[x] + ret
            di[prev] = 0
            return di[x]
        di={x:1 for x in nums}
        if len(nums)==0:return 0
        for x in di:
            check_left(x, di)
        return max(di.values())

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(4, get_sol().longestConsecutive([3,1,4,2]))
    def test02(self):
        self.assertEqual(9, get_sol().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    def test03(self):
        self.assertEqual(3, get_sol().longestConsecutive([0,2,0,1]))
    def test04(self):
        self.assertEqual(0, get_sol().longestConsecutive([]))
