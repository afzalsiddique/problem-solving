import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List


class Solution:
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

class tester(unittest.TestCase):
    def test1(self):
        s = "25525511135"
        Output= ["255.255.11.135","255.255.111.35"]
        self.assertEqual(Output,Solution().restoreIpAddresses(s))
    def test2(self):
        s = "0000"
        Output= ['0.0.0.0']
        self.assertEqual(Output,Solution().restoreIpAddresses(s))
    def test3(self):
        s = "1111"
        Output= ["1.1.1.1"]
        self.assertEqual(Output,Solution().restoreIpAddresses(s))
    def test4(self):
        s = "101023"
        Output= ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
        self.assertEqual(Output,Solution().restoreIpAddresses(s))
    def test5(self):
        s = "010010"
        Output=["0.10.0.10","0.100.1.0"]
        self.assertEqual(Output,Solution().restoreIpAddresses(s))
