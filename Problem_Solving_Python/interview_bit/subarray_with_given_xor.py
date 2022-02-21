from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
def get_sol(): return Solution()

# check out leetcode 560
class Solution:
    def solve(self, nums:List[int], k:int):
        n = len(nums)
        di,ans=defaultdict(int),0
        pre=[0] * n
        pre[0] = nums[0]
        for i in range(1,n):
            pre[i] = pre[i-1]^nums[i]
        for i in range(n):
            if pre[i]==k:ans+=1
            y= pre[i]^k
            if y in di:
                ans+=di[y]
            di[pre[i]]+=1
        return ans

    # compare with count number sub arrays given sum
    # 6  +  8 = 14    14  -  8 = 6     14  -  6 = 8
    # 6 xor 8 = 13    13 xor 6 = 8     13 xor 8 = 6

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(4, get_sol().solve([4, 2, 2, 6, 4], 6))
    def test02(self):
        self.assertEqual(2, get_sol().solve([5, 6, 7, 8, 9], 5))
