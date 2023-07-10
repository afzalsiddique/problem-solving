from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize


dp={}
def prime_factorization(n):
    if n==1: return {2:0}
    if n==6:
        pass
    factors = {}
    i = 2

    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors[i]=factors.get(i,0)+1

    if n > 1:
        factors[i]=factors.get(i,0)+1

    return factors



def func(a,b,c):
    M=2**30
    res=0
    for i in range(1,a+1):
        for j in range(1,b+1):
            for k in range(1,c+1):
                x = i * j * k
                factors=prime_factorization(x)
                cnt=1
                for val in factors.values():
                    cnt*=(val+1)
                print('val:',x,'cnt',cnt,'fact',factors)
                res+=cnt
                res%=M
    print(res)

# a,b,c=list(map(int,input().split()))
# func(a,b,c)

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual( 51103588 , func(100,100,100))
    def test02(self):
        self.assertEqual(20, func(2,2,2))
    def test03(self):
        self.assertEqual(1520, func(5,6,7))
