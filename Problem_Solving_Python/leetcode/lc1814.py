import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # The condition can be rearranged to (nums[i] - rev(nums[i])) == (nums[j] - rev(nums[j])).
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9+7
        li = [x-int(''.join(reversed(str(x)))) for x in nums]
        count = Counter(li)
        ans = 0
        for x,cnt in count.items():
            ans += cnt*(cnt-1)//2
            ans %= MOD
        return ans
class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums = [42,11,1,97]
        Output= 2
        self.assertEqual(Output, get_sol().countNicePairs(nums))
    def test_2(self):
        nums = [13,10,35,24,76]
        Output= 4
        self.assertEqual(Output, get_sol().countNicePairs(nums))
    # def test_3(self):
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
