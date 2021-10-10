import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        sett1 = set(nums1)
        sett2 = set(nums2)
        sett3 = set(nums3)
        res = []
        count = Counter()
        for x in sett1: count[x]+=1
        for x in sett2: count[x]+=1
        for x in sett3: count[x]+=1
        for x in count:
            if count[x]>=2:
                res.append(x)
        return res


class MyTestCase(unittest.TestCase):
    def test1(self):
        nums1,nums2,nums3 = [1,1,3,2],  [2,3], [3]
        Output= sorted([3,2])
        self.assertEqual(Output, sorted(get_sol().twoOutOfThree(nums1,nums2,nums3)))
    def test2(self):
        nums1,nums2,nums3 = [3,1],  [2,3], [1,2]
        Output= sorted([2,3,1])
        self.assertEqual(Output, sorted(get_sol().twoOutOfThree(nums1,nums2,nums3)))
    def test3(self):
        nums1,nums2,nums3 = [1,2,2],  [4,3,3], [5]
        Output= sorted([])
        self.assertEqual(Output, sorted(get_sol().twoOutOfThree(nums1,nums2,nums3)))
    # def test4(self):
    # def test5(self):
    # def test6(self):
