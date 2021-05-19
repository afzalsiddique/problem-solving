import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
# def get_sol(): return Solution()

li = ['1324','hsdgasdf','1','sfdsfhdsf']
li = sorted(li,key=lambda x:len(x))
idx =bisect_left(li,'1')
print(idx)