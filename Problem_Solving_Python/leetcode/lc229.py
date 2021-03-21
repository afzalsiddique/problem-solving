# https://www.youtube.com/watch?v=yDbkQd9t2ig
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1,count2,candidate1,candidate2=0,0,0,1
        for num in nums:
            if num==candidate1:
                count1+=1
            elif num==candidate2:
                count2+=1
            elif count1==0:
                candidate1=num
                count1+=1
            elif count2==0:
                candidate2 = num
                count2+=1
            else:
                count1-=1
                count2-=1
        cnt1,cnt2=0,0
        for num in nums:
            if num==candidate1:cnt1+=1
            elif num==candidate2:cnt2+=1
        res=[]
        if cnt1>len(nums)//3:res.append(candidate1)
        if cnt2>len(nums)//3:res.append(candidate2)
        return res

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        nums = [3,2,3]
        actual = solution.majorityElement(nums)
        expected = [3]
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        nums = [1]
        actual = solution.majorityElement(nums)
        expected = [1]
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        nums = [1,2]
        actual = solution.majorityElement(nums)
        expected = [1,2]
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        nums = [2,2,1,3]
        actual = solution.majorityElement(nums)
        expected = [2]
        self.assertEqual(expected, actual)



