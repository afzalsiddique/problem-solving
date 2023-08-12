from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional,Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
class Solution:
    def SieveOfEratosthenes(self,n):
        prime=[True]*(n+1)
        p=2
        while p*p<=n:
            if prime[p]:
                for i in range(p*p,n+1,p):
                    prime[i]=False
            p+=1
        return prime

class Correct:
    def SieveOfEratosthenes(self,n):
        prime = [True for i in range(n+1)]
        p = 2
        while (p * p <= n):
            if prime[p]:
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1
        return prime


class Tester(unittest.TestCase):
    def test01(self):
        n=1000000
        self.assertEqual(Correct().SieveOfEratosthenes(n), Solution().SieveOfEratosthenes(n))
