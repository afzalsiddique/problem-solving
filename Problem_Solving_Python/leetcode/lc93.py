from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start, parts, path):
            if not parts:
                if start!=n: return
                res.append(path)
                return
            for i in range(start+1,n+1):
                if i-start>=2 and s[start]=='0': continue
                num=int(s[start:i])
                if 0<=num<=255:
                    backtrack(i, parts - 1, path + [num])



        n=len(s)
        res=[]
        backtrack(0,4,[])
        res=[[str(x) for x in ans] for ans in res]
        res=list(map('.'.join,res))
        return res
class Solution2:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def valid(s):
            if s=='': return False
            if s=='0': return True
            if s[0]=='0': return False # string starts with 0
            return 0<=int(s)<=255
        def backtrack(s,n,path):
            if s=='' and n==0:
                res.append(path)
                return
            if s=='' and n>0: return
            if len(s)>0 and n==0: return
            for i in range(min(3,len(s))):
                first,second=s[:i+1],s[i+1:]
                if valid(first):
                    backtrack(second,n-1,path+[first])
        backtrack(s,4,[])
        res=list(map('.'.join,res))
        return res


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(sorted(["255.255.11.135","255.255.111.35"]),sorted(get_sol().restoreIpAddresses("25525511135")))
    def test02(self):
        self.assertEqual(sorted(['0.0.0.0']),sorted(get_sol().restoreIpAddresses("0000")))
    def test03(self):
        self.assertEqual(sorted(["1.1.1.1"]),sorted(get_sol().restoreIpAddresses("1111")))
    def test04(self):
        self.assertEqual(sorted(["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]),sorted(get_sol().restoreIpAddresses("101023")))
    def test05(self):
        self.assertEqual(sorted(["0.10.0.10","0.100.1.0"]),sorted(get_sol().restoreIpAddresses("010010")))
