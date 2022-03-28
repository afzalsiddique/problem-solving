import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools;from sortedcontainers import SortedList
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution2()
class Solution:
    # wrong but helpful to understand the next solution
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        if n==0 or k<=0: return
        curIdx=0
        startIdx=0
        numToBeRotated=nums[startIdx]
        cnt=0
        while True:
            nxtIdx=(curIdx+k)%n
            nxt = nums[nxtIdx]
            nums[nxtIdx]=numToBeRotated
            numToBeRotated = nxt
            curIdx = nxtIdx
            cnt+=1
            if curIdx==startIdx:
                break
        if cnt==n:
            return

        curIdx=1
        startIdx=1
        numToBeRotated=nums[startIdx]
        while True:
            nxtIdx=(curIdx+k)%n
            nxt = nums[nxtIdx]
            nums[nxtIdx]=numToBeRotated
            numToBeRotated = nxt
            curIdx = nxtIdx
            cnt+=1
            if curIdx==startIdx:
                break
class Solution2:
    # time O(n) space O(1)
    # Q: When we finish one cycle, how can we guarantee start++ will start a new cycle? What if start++ is in the middle of the previous cycle?
    # A: Prove by contradiction. If it doesn't start a new cycle then it means that start+1 is in the same cycle as
    # start. Note that if you can reach start+1 from start, then you can also reach start+2 from start+1,
    # meaning that start+2 is also in the same cycle. As a result, the whole array should be accessible within the
    # first cycle, which means that cntRotated reaches n after you finished the first cycle. But to start a new cycle
    # cntRotated is required to be less than n.
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        if n==0 or k<=0: return
        curIdx=0
        startIdx=0
        numToBeRotated=nums[startIdx]
        for _ in range(n):
            nxtIdx=(curIdx+k)%n
            nxt = nums[nxtIdx]
            nums[nxtIdx]=numToBeRotated
            numToBeRotated = nxt
            curIdx = nxtIdx


            # all even indices has been covered. Now cover odd indices.
            # Update: This idea is wrong. But the idea that there are different types of indices still holds true

            # First cover indices-> (0*k  )%n, (1*k  )%n, (2*k  )%n, (3*k  )%n
            # Then cover indices -> (0*k+1)%n, (1*k+1)%n, (2*k+1)%n, (3*k+1)%n
            # Then cover indices -> (0*k+2)%n, (1*k+2)%n, (2*k+2)%n, (3*k+2)%n
            # Then cover indices -> (0*k+3)%n, (1*k+3)%n, (2*k+3)%n, (3*k+3)%n

            # example: [1,2,3,4,5,6,7,8,9], k=3
            # First cover indices -> 0,3,6
            # Then cover indices  -> 1,4,7
            # Then cover indices  -> 2,5,8
            if curIdx==startIdx: # start a new cycle
                curIdx=(curIdx+1)%n
                numToBeRotated = nums[curIdx]
                startIdx+=1
class Solution3:
    # time O(n) space O(n)
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        if n<1: return
        k = k%n
        tmp=[0]*k
        # put the last k elements in a different array
        for i in range(k):
            tmp[i] = nums[n-k+i]

        # put the first (n-k) elements at the end of the array in reverse order. In not done in reverse order,
        # it will overwrite some elements
        for i in range(n-k-1,-1,-1):
            nums[i+k]=nums[i]

        # put the elements of tmp at the beginning of the array
        for i in range(k):
            nums[i]=tmp[i]
class Solution4:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse_nums(start,end):
            while start<end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1

        n=len(nums)
        k=k%n
        reverse_nums(0,n-k-1)
        reverse_nums(n-k,n-1)
        nums.reverse()

class Tester(unittest.TestCase):
    def test01(self):
        nums = [1,2,3,4,5,6,7]; k = 3
        get_sol().rotate(nums,k)
        self.assertEqual( [5,6,7,1,2,3,4],nums)
    def test2(self):
        nums = [1,2,3,4]; k = 2
        get_sol().rotate(nums,k)
        self.assertEqual( [3,4,1,2],nums)
    def test3(self):
        nums = [1]; k = 1
        get_sol().rotate(nums,k)
        self.assertEqual( [1],nums)
    def test4(self):
        nums = [1,2]; k = 2
        get_sol().rotate(nums,k)
        self.assertEqual([1,2],nums)
    def test5(self):
        nums = [-1]; k = 2
        get_sol().rotate(nums,k)
        self.assertEqual([-1],nums)
    def test6(self):
        nums = [1,2,3]; k = 2
        get_sol().rotate(nums,k)
        self.assertEqual([2,3,1],nums)
    def test7(self):
        nums,k = [1,2,3,4,5,6], 3
        get_sol().rotate(nums,k)
        self.assertEqual([4,5,6,1,2,3],nums)
    def test8(self):
        nums,k = [1,2,3,4,5,6,7,8,9], 3
        get_sol().rotate(nums,k)
        self.assertEqual([7,8,9,1,2,3,4,5,6],nums)
    def test9(self):
        nums,k = [3, 8, 9, 7, 6], 3
        get_sol().rotate(nums,k)
        self.assertEqual([9, 7, 6, 3, 8],nums)
