from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def countEven(self, num: int) -> int:
        res=0
        for i in range(1,num+1):
            if self.digitSum(i)&1==0:
                res+=1
        return res

    def digitSum(self,num:int):
        li=[int(x) for x in str(num)]
        return sum(li)

