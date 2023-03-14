from collections import deque;
import unittest; from typing import List;


def get_sol(): return Solution()
class Solution:
    def goodDaysToRobBank(self, nums: List[int], time: int) -> List[int]:
        n=len(nums)
        if time==0: return [i for i in range(n)]
        if n<2*time+1: return []
        left=deque() # non-increasing
        right=deque() # non-decreasing
        for i in range(time):
            while left and nums[i]>left[-1][0]:
                left.pop()
            left.append((nums[i],i))
        for i in range(time+1,time+1+ time):
            while right and nums[i]<right[-1][0]:
                right.pop()
            right.append((nums[i],i))
        res=[]
        for i in range(time,n-time):
            if len(left)==time and len(right)==time and nums[i]<=left[-1][0] and nums[i]<=right[0][0]:
                res.append(i)
            if i==n-time-1:break
            if left and left[0][1]==i-time:
                left.popleft()
            while left and nums[i]>left[-1][0]:
                left.pop()
            left.append((nums[i],i))

            if right and right[0][1]==i+1:
                right.popleft()
            while right and nums[i+time+1]<right[-1][0]:
                right.pop()
            right.append((nums[i+time+1],i+time+1))
        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual([2,3], get_sol().goodDaysToRobBank([5,3,3,3,5,6,2], time = 2))
    def test2(self):
        self.assertEqual([0,1,2,3,4], get_sol().goodDaysToRobBank([1,1,1,1,1], time = 0))
    def test3(self):
        self.assertEqual([], get_sol().goodDaysToRobBank([1,2,3,4,5,6], time = 2))
    def test4(self):
        self.assertEqual([], get_sol().goodDaysToRobBank([1], time = 5))
    def test5(self):
        self.assertEqual([], get_sol().goodDaysToRobBank([1,2,3,4], 1))
    def test6(self):
        self.assertEqual([], get_sol().goodDaysToRobBank([4,3,2,1], 1))
    def test7(self):
        self.assertEqual([5,10,14], get_sol().goodDaysToRobBank([1,2,5,4,1,0,2,4,5,3,1,2,4,3,2,4,8], 2))

