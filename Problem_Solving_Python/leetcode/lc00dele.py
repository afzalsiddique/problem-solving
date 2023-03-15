from itertools import accumulate; from math import floor,ceil,sqrt,log2; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
# from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list

mat=[
    [1,2],
    [3,4]
]
matCpy=tuple(tuple(row[:]) for row in mat)
q=deque(matCpy)
print(q.popleft())