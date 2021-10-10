import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(n1,n2): return FindSumPairs(n1,n2)
class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.count1 = Counter(nums1)
        self.count2 = Counter(nums2)
    def add(self, index: int, val: int) -> None:
        prev=self.nums2[index]
        self.count2[prev]-=1
        self.nums2[index]+=val

        now = self.nums2[index]
        self.count2[now]+=1

    def count(self, tot: int) -> int:
        res=0
        for x in self.count1:
            if tot-x in self.count2:
                res+= self.count1[x]*self.count2[tot-x]
        return res


class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='FindSumPairs':
                obj = get_sol(input[0],input[1])
                outputs.append(None)
            elif cmd=='add':
                outputs.append(obj.add(input[0],input[1]))
            elif cmd=='count':
                outputs.append(obj.count(input[0]))
        return outputs
    def test_01(self):
        commands = ["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
        inputs=[[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]
        expected = [None, 8, None, 2, 1, None, None, 11]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)

#
# class MyTestCase(unittest.TestCase):
#     def test1(self):
#         s = "111000"
#         Output= 1
#         self.assertEqual(Output, get_sol().minSwaps(s))
#     def test2(self):
#         s = "010"
#         Output= 0
#         self.assertEqual(Output, get_sol().minSwaps(s))
#     def test3(self):
#         s = "1110"
#         Output= -1
#         self.assertEqual(Output, get_sol().minSwaps(s))
#     def test4(self):
#         s = "1001"
#         Output= 1
#         self.assertEqual(Output, get_sol().minSwaps(s))
#     def test5(self):
#         s = "100"
#         Output= 1
#         self.assertEqual(Output, get_sol().minSwaps(s))
#     def test6(self):
#         s = "010110"
#         Output= 1
#         self.assertEqual(Output, get_sol().minSwaps(s))
#     # def test7(self):
