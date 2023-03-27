from itertools import accumulate; from math import floor,ceil,sqrt,log2; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
# from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list

def next_greater_element(arr):
    n = len(arr)
    result = [None]*n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            result[arr[stack.pop()]] = arr[i]
        stack.append(i)
    del stack
    return result
li = [4,2,3]
my_sorted_index=sorted(range(len(li)),key=lambda i:li[i])
print(next_greater_element(my_sorted_index))