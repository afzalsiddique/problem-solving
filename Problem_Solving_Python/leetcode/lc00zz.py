from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import *; from a_linked_list import make_linked_list
def binary_search(arr,k):
    n=len(arr)
    lo,hi=0,n-1
    while lo<=hi:
        mid=(lo+hi)//2
        if arr[mid]==k:
            return True
        if arr[mid]>k:
            lo=mid+1
        else:
            hi=mid-1
    return False

