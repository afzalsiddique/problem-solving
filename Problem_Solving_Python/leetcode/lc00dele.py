from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize

def get_moves(x,y):
    return ((x+dx,y+dy) for dx,dy in [(1,0),(1,1),(1,-1)] if 0<=x+dx<m and 0<=y+dy<n)

print(get_moves(0,0))
