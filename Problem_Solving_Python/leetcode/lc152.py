from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()

class Solution4:
    def maxProduct(self, A: List[int]) -> int:
        maxx = A[0]
        minn = A[0]
        res=maxx
        for i in range(1, len(A)):
            tmpMax,tmpMin=maxx,minn
            maxx=max(A[i], A[i] * tmpMax, A[i] * tmpMin)
            minn=min(A[i], A[i] * tmpMax, A[i] * tmpMin)
            res=max(res,maxx)
        return res
class Solution1:
    # https://leetcode.com/problems/maximum-product-subarray/discuss/847520/Thought-process-and-useful-strategy
    # https://www.youtube.com/watch?v=hJ_Uy2DzE08
    def maxProduct(self, A: List[int]) -> int:
        maxx = [A[0]] # these arrays could be removed
        minn = [A[0]]
        for i in range(1, len(A)):
            maxx.append(max(A[i], A[i] * maxx[i - 1], A[i] * minn[i - 1]))
            minn.append(min(A[i], A[i] * maxx[i - 1], A[i] * minn[i - 1]))
        return max(maxx)
class Solution:
    # https://leetcode.com/problems/maximum-product-subarray/discuss/48302/2-Passes-scan-beats-99
    # https://leetcode.com/problems/maximum-product-subarray/discuss/48302/2-Passes-scan-beats-99/706665
    def maxProduct(self, nums: List[int]) -> int:
        product,maxx=1,float('-inf')
        for num in nums:
            product *= num
            maxx=max(maxx, product)
            if num==0:product=1
        product=1
        for num in reversed(nums):
            product*=num
            maxx = max(maxx, product)
            if num==0:product=1
        return maxx

class Solution3:
    # https://leetcode.com/problems/maximum-product-subarray/discuss/48302/2-Passes-scan-beats-99/706665
    def maxProduct(self, nums: List[int]) -> int:
        neg ,maxx= 0,float('-inf')
        for num in nums:
            if num<0:neg+=1
        if neg==1 and len(nums)==1:return nums[0]
        if neg%2==0:
            product = 1
            for num in nums:
                product*=num
                maxx = max(maxx, product)
                if num==0:product=1
            product = 1
            for num in reversed(nums):
                product*=num
                maxx = max(maxx, product)
                if num==0:product=1
            return maxx
        else:
            product,cnt = 1,0
            for num in nums:
                if num<0:cnt+=1
                if cnt==neg:break # take all numbers upto (not including) the last negative number
                product*=num
                maxx = max(maxx, product)
                if num==0:product=1
            product,cnt = 1,0
            for num in reversed(nums):
                if num<0:cnt+=1
                if cnt==neg:break # take all numbers up to (not including) the first negative number
                product*=num
                maxx=max(maxx, product)
                if num==0:product=1
        return maxx

class MyTestCase(unittest.TestCase):
    def test01(self):
        nums = [2,3,-2,4]
        actual = get_sol().maxProduct(nums)
        expected = 6
        self.assertEqual(expected, actual)
    def test02(self):
        nums = [2,3,-2,4, 0, 2,3,-2,4,-5]
        actual = get_sol().maxProduct(nums)
        expected = 240
        self.assertEqual(expected, actual)
    def test03(self):
        nums = [-2,0,-1]
        actual = get_sol().maxProduct(nums)
        expected = 0
        self.assertEqual(expected, actual)
    def test04(self):
        nums = [-2]
        actual = get_sol().maxProduct(nums)
        expected = -2
        self.assertEqual(expected, actual)
    def test05(self):
        nums = [-1,-2,-3]
        actual = get_sol().maxProduct(nums)
        expected = 6
        self.assertEqual(expected, actual)
    def test06(self):
        nums = [2,-5,-2,-4,3]
        actual = get_sol().maxProduct(nums)
        expected = 24
        self.assertEqual(expected, actual)
    def test07(self):
        self.assertEqual(6, get_sol().maxProduct([-1,-2,-3,0]))
    def test08(self):
        self.assertEqual(2, get_sol().maxProduct([-1,0,-2,2]))
