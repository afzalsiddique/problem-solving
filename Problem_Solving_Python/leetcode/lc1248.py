import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/count-number-of-nice-subarrays/discuss/419378/JavaC%2B%2BPython-Sliding-Window-O(1)-Space
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.at_most(nums,k)-self.at_most(nums,k-1)
    def at_most(self, A, k):
        n=len(A)
        odd_cnt=0
        left=right=0
        ans=0
        while right<n:
            if A[right]%2:
                odd_cnt+=1
            while odd_cnt>k:
                if A[left]%2:
                    odd_cnt-=1
                left+=1
            right+=1
            ans+=right-left+1
        return ans
class Solution2:
    # https://leetcode.com/problems/count-number-of-nice-subarrays/discuss/419378/JavaC++Python-Sliding-Window-O(1)-Space/458655
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        i=0
        j=0
        odd_cnt=0
        count=0
        ans=0
        while j<n:
            if nums[j]%2:
                odd_cnt+=1
                count=0
                while odd_cnt==k:
                    if nums[i]%2==0:
                        count+=1
                    else:
                        odd_cnt-=1
                        count+=1
                    i+=1
            ans+=count
            j+=1
        return ans
class Solution3:
    # Replace even elements with 0 and odd elements with 1.
    # The problem is then reduced to the number of subarrays with sum k.
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        for i,x in enumerate(nums):
            nums[i]=nums[i]%2
        i=0
        j=0
        summ=0
        ans=0
        count=0
        while j<n:
            if nums[j]==1:
                summ+=1
                count=0
                while summ==k:
                    if nums[i]==0:
                        count+=1
                    else:
                        summ-=1
                        count+=1
                    i+=1
            ans+=count
            j+=1
        return ans


class tester(unittest.TestCase):
    def test_1(self):
        nums = [1,1,2,1,1]
        k = 3
        Output= 2
        self.assertEqual(Output,get_sol().numberOfSubarrays(nums,k))
    def test_2(self):
        nums = [2,4,6]
        k = 1
        Output= 0
        self.assertEqual(Output,get_sol().numberOfSubarrays(nums,k))
    def test_3(self):
        nums = [2,2,2,1,2,2,1,2,2,2]
        k = 2
        Output= 16
        self.assertEqual(Output,get_sol().numberOfSubarrays(nums,k))
    def test_4(self):
        nums = [1,1,2,2,1,2,1,1,1,2,1,2,2,2,1,1]
        k = 1
        Output= 28
        self.assertEqual(Output,get_sol().numberOfSubarrays(nums,k))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
