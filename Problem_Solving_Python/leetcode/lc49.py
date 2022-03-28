from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        li = []
        for word in strs:
            li.append("".join(sorted(word)))
        di = {}
        for i, word in enumerate(li):
            if word not in di:
                di[word] = [strs[i]]
            else:
                di[word] += [(strs[i])]
        groups = []
        for key in di:
            groups.append(di[key])
        return groups
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def createCount(s:str)->dict:
            count={c:0 for c in string.ascii_lowercase}
            for c in s:
                count[c]+=1
            return count
        def serialize(count:dict)->str:
            li=[]
            for c in string.ascii_lowercase:
                li.append(str(count[c]))
            return ','.join(li)

        di=defaultdict(list) # key: str(serialized), value:List[str]
        for s in strs:
            count=createCount(s)
            serialized = serialize(count)
            di[serialized].append(s)

        return [x for x in di.values()]
class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(sorted([["bat"],["nat","tan"],["ate","eat","tea"]]), sorted(get_sol().groupAnagrams(["eat","tea","tan","ate","nat","bat"])))
    def test02(self):
        self.assertEqual([[""]], get_sol().groupAnagrams([""]))
    def test03(self):
        self.assertEqual([["a"]], get_sol().groupAnagrams(["a"]))
