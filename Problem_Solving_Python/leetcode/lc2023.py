import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = Counter(nums)
        ans = 0
        for prefix in count:
            if target.startswith(prefix):
                suffix = target[len(prefix):]

                if prefix==suffix:
                    ans += count[prefix] * (count[suffix]-1)
                else:
                    ans += count[prefix] * count[suffix]

        return ans

class MyTestCase(unittest.TestCase):
    def test1(self):
        nums = ["777","7","77","77"]
        target = "7777"
        Output= 4
        self.assertEqual(Output, get_sol().numOfPairs(nums,target))
    def test2(self):
        nums = ["123","4","12","34"]
        target = "1234"
        Output= 2
        self.assertEqual(Output, get_sol().numOfPairs(nums,target))
    def test3(self):
        nums = ["1","1","1"]
        target = "11"
        Output= 6
        self.assertEqual(Output, get_sol().numOfPairs(nums,target))
    def test4(self):
        nums = ["123",'123','123',"4",'4','4','4',"12",'12',"34",'34','34']
        target = "1234"
        Output= 18
        self.assertEqual(Output, get_sol().numOfPairs(nums,target))
    def test5(self):
        nums = ["1","1",  "1","1",  "1","1",  "1","1"]
        target = "11"
        Output= 56
        self.assertEqual(Output, get_sol().numOfPairs(nums,target))
    # def test6(self):
