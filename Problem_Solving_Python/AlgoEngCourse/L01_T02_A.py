from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from L01_T01_A import TreeNode,main

def level_order(node:TreeNode)->str:
    if not node: return ""
    li = []
    q = deque([node])
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            li.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
    return my_print(li)

def my_print(li:Optional[List]):
    if not li: return ''
    return ' '.join(map(str,li))