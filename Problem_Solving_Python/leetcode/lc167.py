from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # two pointers
    def twoSum(self, A: List[int], target: int) -> List[int]:
        n=len(A)
        i,j=0,n-1
        res=[-1,-1]
        while i<j:
            if A[i]+A[j]>target:
                j-=1
            elif A[i]+A[j]<target:
                i+=1
            else:
                return [i+1,j+1]
class Solution3:
    # dict
    def twoSum(self, numbers, target):
        dic = {}
        for i, num in enumerate(numbers):
            if target - num in dic:
                return [dic[target - num] + 1, i + 1]
            dic[num] = i
class Solution2:
    # binary search
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            new_target = target - numbers[i]
            tmp = numbers[:i] + numbers[i + 1:]
            idx = bisect_left(tmp, new_target)
            if idx != len(tmp) and tmp[idx] == new_target:
                return [i + 1, idx + 2] # we need to return idx+2. because len(temp) = len(numbers)-1



class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual([1, 2], get_sol().twoSum([2, 7, 11, 15],9))
    def test02(self):
        self.assertEqual([1, 3], get_sol().twoSum([2, 3, 4],6))
    def test03(self):
        self.assertEqual([1, 2], get_sol().twoSum([-1, 0],-1))
    def test04(self):
        self.assertEqual([3, 6], get_sol().twoSum([3,24,50,79,88,150,345],200))
    def test05(self):
        self.assertEqual([2,3], get_sol().twoSum([5,25,75],100))