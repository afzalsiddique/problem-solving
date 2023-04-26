import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution3()
class Solution2:
    # use treemap or map in other languages
    pass
class Solution:
    # https://leetcode.com/problems/odd-even-jump/discuss/1461211/DP-%2B-Stack-%2B-Images-or-O(N*logN)-or-96.54-Faster-or-Combination-of-Generic-Problems
    def oddEvenJumps(self, arr: List[int]) -> int:
        n=len(arr)
        next_higher,next_lower=[-1 for _ in range(n)],[-1 for _ in range(n)]
        next_higher[-1]=n-1
        next_lower[-1]=n-1

        li = sorted([a, i] for i, a in enumerate(arr))
        st=[]
        for a,i in li:
            while st and st[-1]<i:
                next_higher[st.pop()]=i
            st.append(i)

        li = sorted([-a, i] for i, a in enumerate(arr))
        st=[]
        for a,i in li:
            while st and st[-1]<i:
                next_lower[st.pop()]=i
            st.append(i)

        higher, lower = [0] * n, [0] * n
        higher[-1] = lower[-1] = 1
        for i in range(n - 1)[::-1]:
            if next_higher[i]!=-1:
                higher[i] = lower[next_higher[i]]
            if next_lower[i]!=-1:
                lower[i] = higher[next_lower[i]]
        return sum(higher)

class Solution3:
    # https://leetcode.com/problems/odd-even-jump/discuss/1461211/DP-%2B-Stack-%2B-Images-or-O(N*logN)-or-96.54-Faster-or-Combination-of-Generic-Problems
    def oddEvenJumps(self, arr: List[int]) -> int:
        # this function finds next greater index. since it is sorted in ascending order, the next greater index
        # in this case will be the next smallest element of the greater elements in the smallest index.
        # also when sorted in descending order, it will find next smaller element of the smaller elements in the smallest index
        # check other solution for details
        def next_greater_index(indices):
            n = len(indices)
            result = [None]*n
            stack = []
            for i in range(n):
                while stack and indices[stack[-1]] < indices[i]:
                    result[indices[stack.pop()]] = indices[i]
                stack.append(i)
            return result

        if not arr: return 0
        n = len(arr)
        arr_sorted = sorted(range(n), key=lambda x: arr[x])
        nxt_higher = next_greater_index(arr_sorted)

        arr_sorted.sort(key=lambda x: arr[x], reverse=True)
        nxt_lower = next_greater_index(arr_sorted)
        print(nxt_lower)

        odd=[0]*n
        even=[0]*n

        # Last Index is always reachable.
        odd[-1]=1
        even[-1]=1

        for i in range(n-2, -1, -1):

            # If Odd Jump is possible
            if nxt_higher[i] is not None:
                odd[i] = even[nxt_higher[i]]

            # If Even Jump is possible
            if nxt_lower[i] is not None:
                even[i] = odd[nxt_lower[i]]

        return sum(odd) # first jump in odd

class MyTestCase(unittest.TestCase):
    def test1(self):
        actual = get_sol().oddEvenJumps(arr = [10,13,12,14,15])
        Output= 2
        self.assertEqual(Output, actual)
    def test2(self):
        actual = get_sol().oddEvenJumps(arr = [2,3,1,1,4])
        Output= 3
        self.assertEqual(Output, actual)
    def test3(self):
        actual = get_sol().oddEvenJumps(arr = [5,1,3,4,2])
        Output= 3
        self.assertEqual(Output, actual)
    def test4(self):
        actual = get_sol().oddEvenJumps(arr = [1,2,3,2,1,4,4,5])
        Output= 6
        self.assertEqual(Output, actual)
