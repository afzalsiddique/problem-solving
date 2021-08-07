import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
li=[1,2,3,4]
li.extend([1]+list(reversed(li)))
print(li)