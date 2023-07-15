import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution3()
class Solution2:
    # use treemap or map in other languages
    pass
class Solution:
    # https://leetcode.com/problems/odd-even-jump/discuss/1461211/DP-%2B-Stack-%2B-Images-or-O(N*logN)-or-96.54-Faster-or-Combination-of-Generic-Problems
    def nextGreaterOrEqual(self,arr):
        # higher or equal value on the right with the smallest index. basically it is the immediate next element in a sorted array
        n=len(arr)
        next_higher=[-1 for _ in range(n)]
        li = sorted([a, i] for i, a in enumerate(arr))
        st=[]
        for a,i in li:
            # since it is sorted based on value, we can just check whether it is on the right
            # then this will be the larger or equal value on the right side with smallest index
            while st and st[-1]<i:
                next_higher[st.pop()]=i
            st.append(i)
        return next_higher
    def nextLessOrEqual(self,arr):
        # lower or equal value on the right with the smallest index. basically it is the immediate previous element in a sorted array
        n=len(arr)
        next_lower=[-1 for _ in range(n)]
        li = sorted([-a, i] for i, a in enumerate(arr))
        st=[]
        for a,i in li:
            while st and st[-1]<i:
                next_lower[st.pop()]=i
            st.append(i)
        return next_lower
    def oddEvenJumps(self, arr: List[int]) -> int:
        n=len(arr)
        next_higher=self.nextGreaterOrEqual(arr)
        next_lower=self.nextLessOrEqual(arr)

        successfulOddStartingPoints , successfulEvenStartingPoints = [0] * n, [0] * n
        successfulOddStartingPoints [-1] = successfulEvenStartingPoints[-1] = True # we can successfully jump from the end to the end. coz this is the end
        for i in range(n - 1)[::-1]:
            if next_higher[i]!=-1: # if jump possible
                successfulOddStartingPoints [i] = successfulEvenStartingPoints[next_higher[i]]
            if next_lower[i]!=-1:
                successfulEvenStartingPoints[i] = successfulOddStartingPoints [next_lower[i]]
        return sum(successfulOddStartingPoints )

class Solution3:
    # https://leetcode.com/problems/odd-even-jump/discuss/1461211/DP-%2B-Stack-%2B-Images-or-O(N*logN)-or-96.54-Faster-or-Combination-of-Generic-Problems
    def oddEvenJumps(self, arr: List[int]) -> int:
        # this function finds next greater index. since it is sorted in ascending order, the next greater index
        # in this case will be the next smallest element of the greater elements in the smallest index.
        # also when sorted in descending order, it will find next smaller element of the smaller elements in the smallest index
        # check other solution for details
        def next_greater_index(indices):
            n = len(indices)
            result = [-1]*n
            stack = []
            for i in range(n):
                while stack and indices[stack[-1]] < indices[i]:
                    result[indices[stack.pop()]] = indices[i]
                stack.append(i)
            return result

        if not arr: return 0
        n = len(arr)
        arr_sorted = sorted(range(n), key=lambda x: arr[x])
        next_higher = next_greater_index(arr_sorted)

        arr_sorted.sort(key=lambda x: arr[x], reverse=True)
        next_lower = next_greater_index(arr_sorted)

        successfulOddStartingPoints , successfulEvenStartingPoints = [0] * n, [0] * n
        successfulOddStartingPoints [-1] = successfulEvenStartingPoints[-1] = True # we can successfully jump from the end to the end. coz this is the end
        for i in range(n - 1)[::-1]:
            if next_higher[i]!=-1: # if jump possible
                successfulOddStartingPoints [i] = successfulEvenStartingPoints[next_higher[i]]
            if next_lower[i]!=-1:
                successfulEvenStartingPoints[i] = successfulOddStartingPoints [next_lower[i]]
        return sum(successfulOddStartingPoints )

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(2, get_sol().oddEvenJumps(arr = [10,13,12,14,15]))
    def test02(self):
        self.assertEqual(3, get_sol().oddEvenJumps(arr = [2,3,1,1,4]))
    def test03(self):
        self.assertEqual(3, get_sol().oddEvenJumps(arr = [5,1,3,4,2]))
    def test04(self):
        self.assertEqual(6, get_sol().oddEvenJumps(arr = [1,2,3,2,1,4,4,5]))
