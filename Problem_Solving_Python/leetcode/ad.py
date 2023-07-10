# from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
# from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
# from Problem_Solving_Python.template.binary_tree import deserialize,serialize

# approach
# write a function to count divisor of a number
# there is a chance of repeating numbers. so use dynamic programmin

dp={}
def count_divisors(n):
    if n in dp:
        return dp[n]
    count = 0
    i=1
    while i*i<=n:
        if n % i == 0:
            if i == n // i:
                count += 1
            else:
                count += 2
        i+=1
    dp[n]=count
    return count


def func(a,b,c):
    M=2**30
    res=0
    for i in range(1,a+1):
        for j in range(1,b+1):
            for k in range(1,c+1):
                x = i * j * k
                res+=count_divisors(x)
                res%=M
    print(res)

a,b,c=list(map(int,input().split()))
func(a,b,c)
# class MyTestCase(unittest.TestCase):
#     def test01(self):
#         self.assertEqual( 51103588 , func(100,100,100))
#     def test02(self):
#         self.assertEqual(20, func(2,2,2))
#     def test03(self):
#         self.assertEqual(1520, func(5,6,7))
