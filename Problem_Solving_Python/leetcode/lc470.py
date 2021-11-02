import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
def rand7():
    return random.randint(1,7)


class Solution:
    def rand10(self)->int:
        result = float('inf')
        while result > 39: # accept in range [0,39]
            a = rand7()-1 # a in [0,6] inclusive
            b = rand7()-1 # b in [0,6] inclusive
            result = 7*a+b # result in [0,48]
            # 0-> 0%10, 10%10, 20%10, 30%10, 40%10 = 5
            # 1-> 1%10, 11%10, 21%10, 31%10, 41%10 = 5
            # 2-> 2%10, 12%10, 22%10, 32%10, 42%10 = 5
            # 3-> 3%10, 13%10, 23%10, 33%10, 43%10 = 5
            # 4-> 4%10, 14%10, 24%10, 34%10, 44%10 = 5
            # 5-> 5%10, 15%10, 25%10, 35%10, 45%10 = 5
            # ...
            # 9-> 9%10, 19%10, 29%10, 39%10        = 4    49 is out of range
            # uneven distribution
            # reject samples greater than 39 to make the distribution even.
        return result % 10 + 1

class Solution2:
    def rand10(self)->int:
        result = float('inf')
        while result > 47:
            a = rand7() # a in [1,7] inclusive
            b = rand7() # b in [1,7] inclusive
            result = 7*a+b # result in [8,56]
            # reject samples greater than 47 to make the distribution even.
        return result % 10 + 1

class Solution3:
    # wrong ans. check why it is wrong.
    def rand10(self)->int:
        result = float('inf')
        while result > 9:
            a = rand7()-1 # a in [0,6] inclusive
            b = rand7()-1 # b in [0,6] inclusive
            result = a+b # result in [0,12]
            # 0->  (0+0)%10, (5+5)%10,  (4+6)%10, (6+4)%10 = 4
            # 1->  (0+1)%10, (1+0)%10                      = 2
            # 2->  (0+2)%10, (1+1)%10, (2+0)%10            = 3
            # 3->  (0+3)%10, (1+2)%10, (2+1)%10, (3,0)%10  = 4
            # uneven distribution
            # no condition can avoid this even distribution
        return result % 10 + 1
class Solution4:
    # bad solution
    def rand10(self)->int:
        tmp = 0
        for i in range(10):
            tmp+=rand7()
        return tmp%10+1

