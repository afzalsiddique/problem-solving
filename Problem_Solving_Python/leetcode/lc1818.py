import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)
        MOD=10**9+7
        arr=sorted(nums1)
        summ=sum([abs(a-b) for a,b in zip(nums1,nums2)])
        res=summ
        for i in range(n):
            summ-=abs(nums1[i]-nums2[i])

            idx=bisect_left(arr,nums2[i])
            if idx!=n and arr[idx]==nums2[i]:
                diff=0
            else:
                if idx!=0:
                    diff=abs(arr[idx-1]-nums2[i])
                else:
                    diff=float('inf')
            res=min(res,summ+diff)

            idx=bisect_right(arr,nums2[i])
            if idx!=n:
                diff=abs(arr[idx]-nums2[i])
            else:
                diff=float('inf')
            res=min(res,summ+diff)

            summ+=abs(nums1[i]-nums2[i])

        return res % MOD
class Solution2:
    ## TLE
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        abs_values = []
        n = len(nums1)
        for n1,n2 in zip(nums1,nums2):
            abs_values.append(abs(n1-n2))
        total = sum(abs_values)
        minn = total
        for i in range(n):
            for j in range(n):
                nums1[i],nums1[j]=nums1[j],nums1[i]
                tmp = abs(nums1[i]-nums2[i])
                if tmp<abs_values[i]:
                    diff = abs(tmp-abs_values[i])
                    minn = min(minn, total-diff)
                nums1[i],nums1[j]=nums1[j],nums1[i]
        return minn

class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums1,nums2 = [1,7,5],[2,3,5]
        Output= 3
        self.assertEqual(Output, get_sol().minAbsoluteSumDiff(nums1,nums2))
    def test_2(self):
        nums1,nums2 = [2,4,6,8,10],[2,4,6,8,10]
        Output= 0
        self.assertEqual(Output, get_sol().minAbsoluteSumDiff(nums1,nums2))
    def test_3(self):
        nums1,nums2 = [1,10,4,4,2,7],[9,3,5,1,7,4]
        Output= 20
        self.assertEqual(Output, get_sol().minAbsoluteSumDiff(nums1,nums2))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
