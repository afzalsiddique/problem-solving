import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
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
        return arr[left+1:right]

class Solution2:
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
    def test_1(self):
        expected = [1,2,3,4]
        actual = get_sol().findClosestElements( arr = [1,2,3,4,5], k = 4, x = 3)
        self.assertEqual(expected, actual)
    def test_2(self):
        expected = [380,390]
        actual = get_sol().findClosestElements( arr = [380,390,420,430,440], k = 2, x = 399)
        self.assertEqual(expected, actual)
    def test_3(self):
        expected = [1,2,3,4]
        actual = get_sol().findClosestElements(arr = [1,2,3,4,5], k = 4, x = -1)
        self.assertEqual(expected, actual)
    def test_4(self):
        expected = [3,4,6,7]
        actual = get_sol().findClosestElements([0,2,2,3,4,6,7,8,9,9], 4, 5)
        self.assertEqual(expected, actual)
    def test_5(self):
        expected = [8,10]
        actual = get_sol().findClosestElements([3,5,8,10],2,15)
        self.assertEqual(expected, actual)
    def test_6(self):
        expected = [1]
        actual = get_sol().findClosestElements([1,3],1,2)
        self.assertEqual(expected, actual)