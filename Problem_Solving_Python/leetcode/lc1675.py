from heapq import *; import unittest; from typing import List;


def get_sol(): return Solution()
class MaxHeap(list):
    def __init__(self): super().__init__()
    def top(self): return -self[0]
    def push(self, val): heappush(self, -val)
    def heappop(self): return -heappop(self)
class Solution:
    # similar to lc 632
    def minimumDeviation(self, nums: List[int]) -> int:
        n=len(nums)
        nums=[x*2 if x%2 else x for x in nums] # multiply each odd number by 2 and keep the even numbers same
        minn=min(nums)
        res=float('inf')

        pq=MaxHeap()
        for i in range(n):
            pq.push(nums[i])

        while len(pq)==len(nums):
            curMax=pq.heappop()
            res=min(res,curMax-minn)
            if curMax%2==0 and curMax!=1:
                tmpVal=curMax//2
                minn=min(minn,tmpVal)
                pq.push(tmpVal)
        return res
class Solution2:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq = MaxHeap()
        minn=float('inf')
        res=float('inf')
        for x in nums:
            num = x if x&1==0 else x*2
            minn=min(minn,num)
            pq.push(num)
        while len(pq)!=0 and pq.top()&1==0:
            tmp=pq.top()
            res=min(res,pq.heappop()-minn)
            minn=min(minn,tmp//2)
            pq.push(tmp//2)
        if len(pq):
            res=min(res,pq.top()-minn)
        return res

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(1, get_sol().minimumDeviation([1,2,3,4]))
    def test2(self):
        self.assertEqual(3, get_sol().minimumDeviation([4,1,5,20,3]))
    def test3(self):
        self.assertEqual(3, get_sol().minimumDeviation([2,10,8]))
    def test4(self):
        self.assertEqual(1, get_sol().minimumDeviation([3,5]))
    # def test5(self):
    # def test6(self):
    # def test7(self):

