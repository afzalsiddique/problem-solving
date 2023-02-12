import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # time O(logn) space O(1)
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def right_closer(left,right):
            if left<0: return True
            if right==len(arr): return False
            return abs(arr[right]-x)<abs(arr[left]-x)

        idx=bisect_left(arr,x)
        left,right=idx,idx
        while right-left-1!=k:
            if right_closer(left,right):
                right+=1
            else:
                left-=1


        # "left+1". we are favoring left because of the condition
        # "integer a is closer to x than an integer b, if |a - x| == |b - x| and a < b"
        # favoring left side made it exclusive
        return arr[left+1:right]

class Solution3:
    # time O(logn) space O(1)
    def findClosestElements(self, A: List[int], k: int, x: int) -> List[int]:
        def left_closer(left,right):
            if left<0:
                return False
            if right>n-1:
                return True
            return abs(A[left]-x)<=abs(A[right]-x)

        n=len(A)
        idx=bisect_left(A,x)
        left,right=idx,idx # both exclusive
        while right-left-1<k:
            if left_closer(left,right):
                left-=1
            else:
                right+=1


        # "left+1". we are favoring left because of the condition
        # "integer a is closer to x than an integer b, if |a - x| == |b - x| and a < b"
        # favoring left side made it exclusive
        return A[left+1:right]
class Solution2:
    # time O(logn) space O(1)
    # https://www.youtube.com/watch?v=J8yLD-x7fBI
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n=len(arr)
        diff=[abs(x-item) for item in arr]
        summ=minn=sum(diff[:k])

        i,start=0,0
        while i+k!=n:
            summ-=diff[i]
            summ+=diff[i+k]
            i+=1

            if summ<minn:
                minn=summ
                start=i
        return arr[start:start+k]

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual([1,2,3,4], get_sol().findClosestElements([1,2,3,4,5], 4, 3))
    def test02(self):
        self.assertEqual([380,390], get_sol().findClosestElements([380,390,420,430,440], 2,  399))
    def test03(self):
        self.assertEqual([1,2,3,4], get_sol().findClosestElements([1,2,3,4,5], 4,  -1))
    def test04(self):
        self.assertEqual([3,4,6,7], get_sol().findClosestElements([0,2,2,3,4,6,7,8,9,9], 4, 5))
    def test05(self):
        self.assertEqual([8,10], get_sol().findClosestElements([3,5,8,10],2,15))
    def test06(self):
        self.assertEqual([1], get_sol().findClosestElements([1,3],1,2))
