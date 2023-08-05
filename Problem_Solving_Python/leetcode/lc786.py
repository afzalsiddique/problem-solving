from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=ZwbSRpPOVHg&t=891s
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        def count(target):
            num,den=arr[0],arr[-1]
            res=0
            i=0
            for j in range(1,n):
                while arr[i]<=target*arr[j]:
                    i+=1
                res+=i
                if i-1>=0 and arr[i-1]*den>arr[j]*num:
                    num=arr[i-1]
                    den=arr[j]
            return [res,num,den]


        n=len(arr)
        lo=0
        hi=1
        while lo<hi:
            mid=(lo+hi)/2
            cnt,num,den=count(mid)
            if cnt==k:
                return [num,den]
            if cnt<k:
                lo=mid
            elif cnt>k:
                hi=mid
class Solution4:
    # https://leetcode.com/problems/k-th-smallest-prime-fraction/discuss/862410/C%2B%2B-Binary-Search-short-and-easy-Faster-than-99
    def kthSmallestPrimeFraction(self,arr, k):
        def getCnt(m):
            # max_f is used to store the maximum fraction less than mid
            max_f = 0.0
            total = 0
            # p and q are used for storing the indices of max fraction
            p, q = 0, 0
            j = 1
            for i in range(n - 1):
                # if this fraction is greater than mid , move denominator rightwards to find a smaller mid
                while j < n and arr[i] > m * arr[j]:
                    j += 1

                # j elements are greater than mid in this row , n-j are smaller , add them to result
                total += n - j

                if j == n:
                    break

                f = float(arr[i]) / arr[j]

                # update max fraction for this mid
                if f > max_f:
                    p = i
                    q = j
                    max_f = f
            return [total,p,q]

        n = len(arr)
        l, r = 0, 1.0

        while l < r:
            m = (l + r) / 2
            total,p,q=getCnt(m)

            if total == k:
                return [arr[p], arr[q]]
            elif total > k:
                r = m
            else:
                l = m

        return []
class Solution2:
    # heap. not good. O(n^2)
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n=len(arr)
        pq=[]
        for i in range(n):
            heappush(pq,(arr[i]/arr[-1],i,n-1))
        res=[None,None]
        while k:
            val,i,j=heappop(pq)
            res=[arr[i],arr[j]]
            if j-1>i:
                heappush(pq,(arr[i]/arr[j-1],i,j-1))
            k-=1
        return res


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual([2,5], get_sol().kthSmallestPrimeFraction([1,2,3,5], 3))
    def test02(self):
        self.assertEqual([1,7], get_sol().kthSmallestPrimeFraction([1,7], 1))
    def test03(self):
        self.assertEqual([13,17], get_sol().kthSmallestPrimeFraction([1,13,17,59], 6))
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):
    # def test11(self):
    #
