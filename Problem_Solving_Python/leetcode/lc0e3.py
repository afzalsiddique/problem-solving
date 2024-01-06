# from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt; import sortedcontainers
# from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list,ListNode
# from Problem_Solving_Python.template.binary_tree import deserialize,serialize
import unittest
import math
import os
import random
import re
import sys

def getSmallestString(s, k):
    result = []
    for i,c in enumerate(s):
        dist_a=circular_distance(c,'a')
        if dist_a<=k:
            result.append('a')
            k-=dist_a
        else:
            new_char=get_min_char(c,k)
            result.append(new_char)
            k-=circular_distance(c,new_char)
    return ''.join(result)




def get_min_char(c,k):
    c_idx=ord(c)-ord('a')
    idx=min((c_idx+k)%26,(c_idx-k)%26)
    return chr(idx+ord('a'))

def circular_distance(char1, char2):
    char1 = char1.upper()
    char2 = char2.upper()
    clockwise_distance = (ord(char2) - ord(char1) + 26) % 26
    counterclockwise_distance = (ord(char1) - ord(char2) + 26) % 26
    return min(clockwise_distance, counterclockwise_distance)



class MyTestCase(unittest.TestCase):
    def test00(self):
        self.assertEqual('ac', getSmallestString('bd',2))
    def test01(self):
        self.assertEqual('cx', getSmallestString('gx',4))
    def test02(self):
        self.assertEqual('aaf', getSmallestString('amk',17))
    def test03(self):
        self.assertEqual(1, circular_distance('a','z'))
    def test04(self):
        self.assertEqual(2, circular_distance('a','c'))
    def test05(self):
        self.assertEqual(1, circular_distance('z','a'))
