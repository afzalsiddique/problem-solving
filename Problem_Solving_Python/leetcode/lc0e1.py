# from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt; import sortedcontainers
# from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list,ListNode
# from Problem_Solving_Python.template.binary_tree import deserialize,serialize
import unittest
import math
import os
import random
import re
import sys

def countSentences(wordSet, sentences):
    wordSet=["".join(sorted(w)) for w in wordSet]
    freq={}
    for w in wordSet:
        if w not in freq:
            freq[w]=1
        else:
            freq[w]+=1
    # print(wordSet)
    # print(freq)

    new_sentences=[]
    for s in sentences:
        s=s.split()
        s=[''.join(sorted(w)) for w in s]
        new_sentences.append(s)

    # print(new_sentences)
    res=[]
    for s in new_sentences:
        tmp=1
        for w in s:
            tmp*=freq[w]
        res.append(tmp)
    return res




class MyTestCase(unittest.TestCase):
    def test00(self):
        self.assertEqual(3, countSentences(['the','bats','tabs','in','cat','act'],['cat the bats',
                                                                                   'in the act','act tabs in']))
    # def test01(self):
    # def test02(self):
    # def test03(self):
    # def test04(self):
