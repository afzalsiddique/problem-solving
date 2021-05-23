import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=FpO3fY-1mj8
    # two pointers
    # time O(n) space O(1)
    def longestMountain(self, arr):
        n=len(arr)
        maxx=0
        for i in range(1,n-1):
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                left,right=i,i
                while left-1>=0 and arr[left-1]<arr[left]:
                    left-=1
                while right+1<n and arr[right+1]<arr[right]:
                    right+=1
                maxx=max(maxx,right-left+1)
        return maxx

class Solution2:
    # https://leetcode.com/problems/longest-mountain-in-array/discuss/135593/C%2B%2BJavaPython-1-pass-and-O(1)-space
    # time O(n) space O(n)
    def longestMountain(self, arr):
        up, down = [0] * len(arr), [0] * len(arr)
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                up[i] = up[i - 1] + 1
        for i in range(len(arr) - 1)[::-1]:
            if arr[i] > arr[i + 1]:
                down[i] = down[i + 1] + 1
        return max([u + d + 1 for u, d in zip(up, down) if u and d] or [0])

class Solution3:
    # tle
    # time O(n^2) space O(n)
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        left = [i for i in range(n)]
        right = [i for i in range(n)]
        for i in range(n):
            j = i
            while j - 1 >= 0:
                if arr[j - 1] < arr[j]:
                    j -= 1
                else:
                    break
            left[i] = j
        for i in range(n):
            j = i
            while j + 1 < n:
                if arr[j + 1] < arr[j]:
                    j += 1
                else:
                    break
            right[i] = j
        # print(left)
        # print(right)
        ans = 0
        for i in range(n):
            temp = right[i] - left[i] + 1
            if left[i]< i < right[i] and temp >= 3 and temp > ans:
                ans = temp
        return ans


class tester(unittest.TestCase):
    def test01(self):
        arr = [2, 1, 4, 7, 3, 2, 5]
        Output = 5
        self.assertEqual(Output, get_sol().longestMountain(arr))

    def test02(self):
        arr = [2, 2, 2]
        Output = 0
        self.assertEqual(Output, get_sol().longestMountain(arr))

    def test03(self):
        arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        Output = 0
        self.assertEqual(Output, get_sol().longestMountain(arr))
