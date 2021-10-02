import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) * 6 < len(nums2) or len(nums1) > len(nums2) * 6:
            return -1
        sm1, sm2 = map(sum, (nums1, nums2))
        if sm1 > sm2:
            return self.minOperations(nums2, nums1)
        cnt = Counter([6 - n for n in nums1] + [n - 1 for n in nums2])
        i, operations = 5, 0
        while sm2 > sm1:
            while cnt[i] == 0:
                i -= 1
            sm1 += i
            cnt[i] -= 1
            operations += 1
        return operations
class Solution2:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1,sum2=sum(nums1),sum(nums2)
        diff = sum1-sum2
        if sum1<sum2: return self.minOperations(nums2,nums1)
        count= Counter()
        for x in nums1: count[x-1]+=1
        for x in nums2: count[6-x]+=1
        steps=0
        while diff>0:
            if not count: return -1
            key=max(count)
            count[key]-=1
            if count[key]==0: count.pop(key)
            diff -= key
            steps+=1
        return steps

class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums1,nums2 = [1,2,3,4,5,6], [1,1,2,2,2,2]
        Output= 3
        self.assertEqual(Output, get_sol().minOperations(nums1,nums2))
    def test_2(self):
        nums1,nums2 = [1,1,1,1,1,1,1], [6]
        Output= -1
        self.assertEqual(Output, get_sol().minOperations(nums1,nums2))
    def test_3(self):
        nums1,nums2 = [6,6], [1]
        Output= 3
        self.assertEqual(Output, get_sol().minOperations(nums1,nums2))
    def test_4(self):
        nums1,nums2 = [5,2,1,5,2,2,2,2,4,3,3,5], [1,4,5,5,6,3,1,3,3]
        Output= 1
        self.assertEqual(Output, get_sol().minOperations(nums1,nums2))
    def test_5(self):
        nums1,nums2 = [2,3], [5]
        Output= 0
        self.assertEqual(Output, get_sol().minOperations(nums1,nums2))
    def test_6(self):
        nums1,nums2 = [3,3,2,4,2,6,2], [6,2,6,6,1,1,4,6,4,6,2,5,4,2,1]
        Output= 8
        self.assertEqual(Output, get_sol().minOperations(nums1,nums2))
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
