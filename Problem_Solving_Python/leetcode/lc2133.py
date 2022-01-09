import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n=len(matrix)
        for i in range(n):
            sett=set()
            for j in range(n):
                if not 1<=matrix[i][j]<=n:
                    return False
                if matrix[i][j] in sett:
                    return False
                sett.add(matrix[i][j])

        for j in range(n):
            sett=set()
            for i in range(n):
                if not 1<=matrix[i][j]<=n:
                    return False
                if matrix[i][j] in sett:
                    return False
                sett.add(matrix[i][j])
        return True


