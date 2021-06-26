import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class Solution:
    def advantageCount(self, A, B):
        n = len(A)
        B = sorted([(num, i) for i, num in enumerate(B)])[::-1]
        A = sorted(A)[::-1]
        ans = [-1]*n

        beg, end = 0, n - 1

        for num, ind in B:
            if A[beg] > num:
                ans[ind] = A[beg]
                beg += 1
            else:
                ans[ind] = A[end]
                end -= 1

        return ans
class Solution2:
    # my original solution
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums1)
        heapify(nums1)
        di = defaultdict(list)
        for i in range(n):
            di[nums2[i]].append(i)
        nums2.sort()
        res = [-1]*n
        left=[] # values of nums2 where advantage is not possible
        not_visited={i for i in range(n)} # indices of nums2 where advantage is not possible
        for x in nums2:
            if not nums1: break
            while nums1 and nums1[0]<=x:
                left.append(heappop(nums1))
            if nums1:
                idx = di[x].pop()
                res[idx] = heappop(nums1)
                not_visited.remove(idx)
        for idx in not_visited:
            res[idx]=left.pop()
        return res
class tester(unittest.TestCase):
    def test1(self):
        nums1 = [2,7,11,15]
        nums2 = [1,10,4,11]
        Output= [2,11,7,15]
        self.assertEqual(Output,get_sol().advantageCount(nums1,nums2))
    def test2(self):
        nums1 = [12,24,8,32]
        nums2 = [13,25,32,11]
        Output= [24,32,8,12]
        self.assertEqual(Output,get_sol().advantageCount(nums1,nums2))
