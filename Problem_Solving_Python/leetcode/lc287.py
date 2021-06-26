# https://www.youtube.com/watch?v=dfIqLxAf-8s
# https://www.youtube.com/watch?v=-YiQZi3mLq0
import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()


class Solution:
    # this will not work if array is in the range [0,n] (inclusive). It has to be [1,n]
    # floyd cycle detection by changing the input array
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                break
        fast = nums[0]
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

class Solution2:
    # this will work even if the array contains 0
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            idx = abs(nums[i])-1 # will work even if the array contains 0
            # idx = abs(nums[i]) # will not work if the array contains 0
            if nums[idx]<0:
                return abs(nums[i])
            else:
                nums[idx]*=-1


class Solution3:
    def findDuplicate(self, nums: List[int]) -> int:
        prev = -1
        cur = 0
        while True:
            if nums[cur]<0: return nums[prev]*(-1)
            nums[cur]*=-1
            prev=cur
            cur=abs(nums[cur])
class MyTestCase(unittest.TestCase):
    def test_10(self):
        expected = 4
        actual = get_sol().findDuplicate([3,4,1,4,2])
        self.assertEqual(expected, actual)
    # good example
    def test_1(self):
        expected = 2
        actual = get_sol().findDuplicate([1,3,4,2,2])
        self.assertEqual(expected, actual)
    def test_11(self):
        expected = 2
        actual = get_sol().findDuplicate([5,2,3,4,2,1])
        self.assertEqual(expected, actual)

    def test_20(self):
        expected = 3
        actual = get_sol().findDuplicate([3,1,3,4,2])
        self.assertEqual(expected, actual)
    def test_2(self):
        expected = 4
        actual = get_sol().findDuplicate([3,4,2,1,4])
        self.assertEqual(expected, actual)

    def test_3(self):
        expected = 1
        actual = get_sol().findDuplicate([1,1])
        self.assertEqual(expected, actual)

    def test_4(self):
        expected = 1
        actual = get_sol().findDuplicate([1,1,2])
        self.assertEqual(expected, actual)