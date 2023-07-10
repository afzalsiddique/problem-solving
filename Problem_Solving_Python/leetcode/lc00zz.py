from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
# def get_sol(): return Solution()
def prime_factorization(n):
    factors = []
    i = 2

    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)

    if n > 1:
        factors.append(n)

    return factors

# Example usage
number = 36
factors = prime_factorization(number)
print(f"The prime factors of {number} are: {factors}")

# class MyTestCase(unittest.TestCase):
#     def test1(self):
#         nums, k = [1,3,-1,-3,5,3,6,7],3
#         Output= [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
#         self.assertEqual(Output, get_sol().medianSlidingWindow(nums,k))
#     def test2(self):
#         nums, k = [1,2,3,4,2,3,1,4,2], 3
#         Output= [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
#         self.assertEqual(Output, get_sol().medianSlidingWindow(nums,k))
#     def test3(self):
#         nums, k = [1,2], 1
#         Output= [1.00000,2.00000]
#         self.assertEqual(Output, get_sol().medianSlidingWindow(nums,k))
#     def test4(self):
#         nums, k = [2147483647,1,2,3,4,5,6,7,2147483647], 2
#         Output= [1073741824.0, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 1073741827.0]
#         self.assertEqual(Output, get_sol().medianSlidingWindow(nums,k))
#     def test5(self):
#         nums, k = [1,3,-1,-3],3
#         Output= [1.00000,-1.00000]
#         self.assertEqual(Output, get_sol().medianSlidingWindow(nums,k))
#     def test6(self):
#         nums, k = [1,3,-1,-3,5,3],3
#         Output= [1.00000,-1.00000,-1.00000,3.00000]
#         self.assertEqual(Output, get_sol().medianSlidingWindow(nums,k))
#     # def test7(self):
#     # def test8(self):
