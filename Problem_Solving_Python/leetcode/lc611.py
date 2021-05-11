import itertools
import math
import operator
import random
from bisect import *
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
def get_sol(): return Solution()


class Solution:
    # https://leetcode.com/problems/valid-triangle-number/discuss/128135/A-similar-O(n2)-solution-to-3-Sum
    # similar to 3 sum problem
    # time O(n^2)
    def triangleNumber(self, nums: List[int]) -> int:
        n,cnt=len(nums),0
        nums.sort()
        for i in reversed(range(2,n)):
            l,r=0,i-1
            while l<r:
                a,b,c = nums[l],nums[r],nums[i]
                if a+b>c:
                    # print(r,l)
                    cnt+=r-l
                    r-=1
                else:
                    l+=1
        return cnt

class Solution2:
    # binary search
    # time O(n^2 * log n)
    def triangleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        cnt=0
        for i in range(n-2):
            for j in range(i+1,n-1):
                a,b=nums[i],nums[j]
                if a==0 or b==0: continue
                k=bisect_left(nums,a+b)
                print(k-j-1)
                cnt+=k-j-1
        return cnt


class tester(unittest.TestCase):
    def test1(self):
        nums = [2,2,3,4]
        Output= 3
        self.assertEqual(Output,Solution().triangleNumber(nums))
    def test2(self):
        nums = [4,2,3,4]
        Output= 4
        self.assertEqual(Output,Solution().triangleNumber(nums))
    def test3(self):
        nums = [1,3,3,4,4,6,7,7,9]
        Output= 40
        self.assertEqual(Output,Solution().triangleNumber(nums))
    def test4(self):
        nums = [2,2,2,3,3,3,4,4,4]
        Output= 75
        self.assertEqual(Output,Solution().triangleNumber(nums))
    def test5(self):
        nums = [1,1,1,1]
        Output= 4
        self.assertEqual(Output,Solution().triangleNumber(nums))
    def test6(self):
        nums = [0,0,0]
        Output= 0
        self.assertEqual(Output,Solution().triangleNumber(nums))
    def test7(self):
        nums = [0,1,0]
        Output= 0
        self.assertEqual(Output,Solution().triangleNumber(nums))
