# https://www.youtube.com/watch?v=vcv3REtIvEo&t=1020s
import unittest
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, n,mx_area= [], len(heights),0
        left,right=[0 for _ in range(n)],[0 for _ in range(n)]

        for i in range(n):
            if not stack:
                left[i]=0 # if stack is empty then there is no left bound which means the left bound is 0
                stack.append(i)
            else:
                while stack and heights[i]<=heights[stack[-1]]: # it's "<=" and not "<". Run this Case: [1,5,5,5,1]
                    stack.pop()
                left[i]=stack[-1]+1 if stack else 0 # if stack is empty then there is no left bound which means the left bound is 0
                stack.append(i)
        print(left)
        stack = []
        for i in reversed(range(n)):
            if not stack:
                right[i]=n-1 # if stack is empty then there is no right bound which means the right bound is n-1
                stack.append(i)
            else:
                while stack and heights[i]<=heights[stack[-1]]:# it's "<=" and not "<". Run this Case: [1,5,5,5,1]
                    stack.pop()
                right[i]=stack[-1]-1 if stack else n-1 # if stack is empty then there is no right bound which means the right bound is n-1
                stack.append(i)
        print(right)
        for i,h in enumerate(heights):
            mx_area = max(mx_area,(right[i]-left[i]+1)*h)
        return mx_area

class MyTestCase(unittest.TestCase):

    def test_1(self):
        actual = Solution().largestRectangleArea([2,1,5,6,2,3])
        expected = 10
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.largestRectangleArea([2,4])
        expected = 4
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.largestRectangleArea([1,1])
        expected = 2
        self.assertEqual(expected, actual)
    def test_4(self):
        sol = Solution()
        actual = sol.largestRectangleArea([1,5,5,5,1])
        expected = 15
        self.assertEqual(expected, actual)
    def test_5(self):
        sol = Solution()
        actual = sol.largestRectangleArea([3,6,5,7,4,8,1,0])
        expected = 20
        self.assertEqual(expected, actual)
