from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *
def get_sol(): return Solution()

# Boyer Moore
# https://www.youtube.com/watch?v=gY-I8uQrCkk
class Solution0:
    def majorityElement(self, nums: List[int]) -> int:
        maj=nums[0]
        cnt = 0
        for num in nums:
            if maj==num:
                cnt+=1
            else:
                if cnt==0:
                    maj=num
                    cnt=1
                else:
                    cnt-=1
        return maj
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = nums[0], 0
        for num in nums:
            if num==candidate:
                count+=1
            else:
                count-=1
                if count==0:
                    candidate=num
                    count+=1
        return candidate

class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 0
        for i in range(len(nums)):
            if count ==0:
                candidate=nums[i]
                count=1
            elif nums[i]==candidate:
                count+=1
            else:
                count-=1
        return candidate
class Solution4:
    def majorityElement(self, nums: List[int]) -> int:
        cand1,cand2=nums[0],nums[0]
        cnt1,cnt2=0,0
        for x in nums:
            if x==cand1:
                cnt1+=1
            elif x==cand2:
                cnt2+=1
            else:
                if cnt1==0:
                    cand1=x
                    cnt1=1
                elif cnt2==0:
                    cand2=x
                    cnt2=1
                else:
                    cnt1-=1
                    cnt2-=1
        return cand1 if cnt1>cnt2 else cand2
class Solution3:
    def majorityElement(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums))[0]

    def helper(self, nums, l, r):
        if l == r - 1:
            return nums[l], 1
        mid = l + (r - l) // 2
        maj_left, extra_left = self.helper(nums, l, mid)
        maj_right, extra_right = self.helper(nums, mid, r)

        if maj_right==maj_left:
            maj = maj_left
            extra = extra_left + extra_right
        elif extra_right > extra_left:
            maj = maj_right
            extra = extra_right - extra_left
        else:
            maj = maj_left
            extra = extra_left - extra_right
        return maj, extra


class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums = [3,2,3]
        actual = get_sol().majorityElement(nums)
        expected = 3
        self.assertEqual(expected, actual)
    def test_2(self):
        nums = [2,2,1,1,1,2,2]
        actual = get_sol().majorityElement(nums)
        expected = 2
        self.assertEqual(expected, actual)
    def test_3(self):
        nums = [6,5,5]
        actual = get_sol().majorityElement(nums)
        expected = 5
        self.assertEqual(expected, actual)
    def test04(self):
        self.assertEqual(100,get_sol().majorityElement([-1,100,2,100,100,4,100]))
