import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76583/11ms-JAVA-solution-using-merge-sort-with-explanation
    def countSmaller(self, nums: List[int]) -> List[int]:
        def mergesort(nums, index, l, r, res):
            if l>=r:
                return
            mid = (l+r)//2
            mergesort(nums, index, l, mid, res)
            mergesort(nums, index, mid+1, r, res)
            merge(nums, index, l, mid, mid+1, r, res)
        def merge(nums, index, l1, r1, l2, r2, res):
            start = l1
            tmp = [0]*(r2-l1+1)
            count = 0
            p = 0
            while l1<=r1 or l2<=r2:
                if l1>r1:
                    tmp[p] = index[l2]
                    p+=1
                    l2+=1
                elif l2>r2:
                    res[index[l1]] += count
                    tmp[p] = index[l1]
                    p+=1
                    l1+=1
                elif nums[index[l1]] > nums[index[l2]]:
                    tmp[p] = index[l2]
                    p+=1
                    l2+=1
                    count+=1
                else:
                    res[index[l1]] += count
                    tmp[p]= index[l1]
                    p+=1
                    l1+=1
            for i in range(len(tmp)):
                index[start+i] = tmp[i]

        res = [0] * len(nums)
        index = [0] * len(res)
        for i in range(len(res)):
            index[i] = i
        mergesort(nums, index, 0, len(nums)-1, res)
        li = []
        for i in res:
            li.append(i)
        return li
class Solution2:
    # https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/408322/Python-Different-Concise-Solutions
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums = nums[::-1]
        min_v = min(nums) if nums else 0

        import collections
        record = collections.defaultdict(int)

        res = []
        for n in nums:
            cnt = 0
            for target in range(min_v,n):
                if target in record:
                    cnt += record[target]
            res.append(cnt)
            record[n]+=1
        return res[::-1]


class MyTestCase(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        nums = [7,8,11,12,13,4,5,6,9,10]
        expected = [3,3,5,5,5,0,0,0,0,0]
        actual = sol.countSmaller(nums)
        self.assertEqual(expected, actual)
    def test_2(self):
        sol = Solution()
        nums = [5,2,6,1]
        expected = [2,1,1,0]
        actual = sol.countSmaller(nums)
        self.assertEqual(expected, actual)
# # https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76583/11ms-JAVA-solution-using-merge-sort-with-explanation
# from typing import List
#
# class Solution:
#     def countSmaller(self, nums: List[int]) -> List[int]:
#         def mergesort(nums, indexes, start, end, count):
#             if end<=start:
#                 return
#             mid = (start + end) //2
#             mergesort(nums, indexes, start, mid, count)
#             mergesort(nums, indexes, mid + 1, end, count)
#             merge(nums, indexes, start, end, count)
#         def merge(nums, indexes, start, end, count):
#             mid = (start + end) // 2
#             left_index = start
#             right_index = mid + 1
#             rightcount = 0
#             new_indexes = [0] * (end-start+1)
#
#             sort_index = 0
#             while left_index <= mid and right_index <= end:
#                 if nums[indexes[right_index]] < nums[indexes[left_index]]:
#                     new_indexes[sort_index] = indexes[right_index]
#                     rightcount+=1
#                     right_index+=1
#                 else:
#                     new_indexes[sort_index] = indexes[left_index]
#                     count[indexes[left_index]] += rightcount
#                     left_index+=1
#                 sort_index+=1
#             while left_index <=mid:
#                 new_indexes[sort_index] = indexes[left_index]
#                 count[indexes[left_index]] += rightcount
#                 left_index+=1
#                 sort_index+=1
#             while right_index <= end:
#                 new_indexes[sort_index] = indexes[right_index]
#                 right_index+=1
#                 sort_index+=1
#             for i in range(start, end):
#                 indexes[i] = new_indexes[i-start]
#
#         res = []
#         count = [0] * len(nums)
#         indexes = [i for i in range(len(nums))]
#         mergesort(nums, indexes, 0, len(nums)-1, count)
#         for i in range(len(nums)):
#             res.append(count[i])
#         return res
