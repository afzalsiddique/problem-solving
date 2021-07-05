import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;


mat = [[1,2,3],[4,5,6],[7,8,9]]
m,n=len(mat),len(mat[0])
for i in range(m):
    mat[i]=[0]+mat[i]
mat=[[0]*(n+1)]+mat

print(mat)
