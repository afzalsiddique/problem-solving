from heapq import *; import unittest; from typing import List;


def get_sol(): return Solution()
class MaxHeap:
    def __init__(self):
        self.data = []
    def top(self): return -self.data[0]
    def push(self, val): heappush(self.data, -val)
    def heappop(self): return -heappop(self.data)
    def __repr__(self): return str(self.data)
    def __len__(self): return len(self.data)
    def __bool__(self): return True if len(self.data) else False

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        mxHeap=MaxHeap()
        for i,x in enumerate(target):
            mxHeap.push(x)
        summ=sum(target)
        while mxHeap:
            if mxHeap.top()<=summ//2:
                break
            cur=mxHeap.heappop()
            if cur==1: # all other elements must be 1
                return True
            other = summ-cur
            if other==0:
                return False
            newCur=cur%other # why mod? -> https://leetcode.com/problems/construct-target-array-with-multiple-sums/discuss/510256/JavaC++Python-Backtrack-OJ-is-wrong/499352
            mxHeap.push(newCur)
            summ=other+newCur
            # alternative
            # summ-=cur
            # summ+=newCur
        return summ==len(target)
class Solution2:
    def isPossible(self, target: List[int]) -> bool:
        mxHeap=MaxHeap()
        for i,x in enumerate(target):
            mxHeap.push(x)
        summ=sum(target)
        while True:
            cur=mxHeap.heappop()
            other=summ-cur
            if cur==1: return True
            if other==1: return True
            if cur<other: return False
            if other==0: return False
            if cur%other==0: return False
            prev=cur%other # why mod? -> https://leetcode.com/problems/construct-target-array-with-multiple-sums/discuss/510256/JavaC++Python-Backtrack-OJ-is-wrong/499352
            summ-=cur
            summ+=prev
            mxHeap.push(prev)

class Tester(unittest.TestCase):
    def test_1(self):
        self.assertEqual(True,get_sol().isPossible([9,3,5]))
    def test_2(self):
        self.assertEqual(False,get_sol().isPossible([1,1,1,2]))
    def test_3(self):
        self.assertEqual(True,get_sol().isPossible([8,5]))
    def test_4(self):
        self.assertEqual(True,get_sol().isPossible([1,1000000000]))
    def test_5(self):
        self.assertEqual(False,get_sol().isPossible([1,1,2]))
    def test_6(self):
        self.assertEqual(True,get_sol().isPossible([1]))
    def test_7(self):
        self.assertEqual(False,get_sol().isPossible([2,4]))
