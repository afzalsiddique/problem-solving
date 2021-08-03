import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/discuss/463222/Java-Binary-search-O(nlogk)-k-is-the-max-value-in-arr
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n=len(arr)
        pre=[0]+list(itertools.accumulate(arr))
        def get_sum_optim(mid): # optimized. requires sorting the arr
            idx = bisect_left(arr,mid)
            return mid*(n-idx)+pre[idx]
        def get_sum(mid): # does not require sorting the arr
            summ = 0
            for a in arr:
                if a>mid:
                    summ+=mid
                else:
                    summ+=a
            return summ

        maxx=max(arr)
        left = 0; right = maxx
        diff=target
        prev_value=maxx
        while left<=right:
            mid=(left+right)//2
            summ=get_sum_optim(mid)
            current_diff=abs(target-summ)
            if current_diff<diff:
                diff=current_diff
                prev_value=mid
            elif current_diff==diff:
                prev_value = min(prev_value, mid)
            if summ > target:
                right = mid - 1
            else:
                left = mid + 1
        return prev_value



class Tester(unittest.TestCase):
    def test_1(self):
        arr,target = [4,9,3],10
        Output= 3
        self.assertEqual(Output,get_sol().findBestValue(arr,target))
    def test_2(self):
        arr,target = [2,3,5],10
        Output= 5
        self.assertEqual(Output,get_sol().findBestValue(arr,target))
    def test_3(self):
        arr,target = [60864,25176,27249,21296,20204],56803
        Output= 11361
        self.assertEqual(Output,get_sol().findBestValue(arr,target))
    def test_4(self):
        arr,target = [2,3,5], 11
        Output= 5
        self.assertEqual(Output,get_sol().findBestValue(arr,target))
    def test_5(self):
        arr,target = [1547,83230,57084,93444,70879], 71237
        Output= 17422
        self.assertEqual(Output,get_sol().findBestValue(arr,target))
    def test_7(self):
        arr,target = [15,1,1,1,1,1,1,1,1,1,1,1], 50
        Output= 15
        self.assertEqual(Output,get_sol().findBestValue(arr,target))
    # def test_8(self):