from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from Problem_Solving_Python.template.binary_tree import deserialize
mat=[[1,2,3],[4,5,6]]
def within(x:int,y:int)->bool:
    return 0<=x<len(mat) and 0<=y<len(mat[0])
def get_4d_moves(x:int, y:int)->List[tuple[int,int]]:
    return [(x+dx,y+dy) for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)] if within(x+dx,y+dy)]
def fromMatToTuple(mat:List[List[int]])->tuple[tuple[int]]:
    return tuple([tuple(row) for row in mat])
def fromTupleToMatrix(tup:tuple[tuple[int]])->List[List[int]]:
    return [list(row) for row in tup]
