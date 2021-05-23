import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
# def get_sol(): return Solution()



permutations=[]
def permute(arr:List[str],path):
    if not arr:
        permutations.append(''.join(path[:]))
        return
    for i in range(len(arr)):
        permute(arr[:i]+arr[i+1:],path+[arr[i]])
arr = [1,5,3,2]
arr = list(map(str,arr))
permute(arr,[])
print(permutations)