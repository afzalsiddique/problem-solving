import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/longest-happy-string/discuss/564277/C%2B%2BJava-a-greater-b-greater-c
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        def helper(lg, med, sm, lg_c, med_c, sm_c):
            if med>lg:
                tmp=helper(med, lg, sm, med_c, lg_c, sm_c)
                return tmp
            if sm>med:
                tmp=helper(lg, sm, med, lg_c, sm_c, med_c)
                return tmp
            if med==0:
                return min(2,lg)*lg_c
            use_lg=min(2,lg)
            if lg-use_lg>=med:
                use_med=1
            else:
                use_med=0
            tmp1=lg_c*use_lg + med_c*use_med
            tmp2=helper(lg-use_lg,med-use_med,sm,lg_c,med_c,sm_c)
            return tmp1+tmp2
        return helper(a,b,c,'a','b','c')
class Solution2:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        def add_to_res():
            res.append(pq[0][1])
            pq[0][0]+=1 # max_heap
            if not pq[0][0]:
                heappop(pq)
        pq=[]
        if a: heappush(pq,[-a,'a'])
        if b: heappush(pq,[-b,'b'])
        if c: heappush(pq,[-c,'c'])
        heapify(pq)
        res=[]
        while True:
            if not pq: break
            if len(res)==0 or len(res)==1:
                add_to_res()
            elif res[-1]!=res[-2]:
                add_to_res()
            elif res[-1]==res[-2]:
                if pq[0][1]!=res[-1]:
                    add_to_res()
                elif len(pq)>=2:
                    tmp = heappop(pq)
                    add_to_res()
                    heappush(pq,tmp)
                else:
                    break
            else:
                break
        return ''.join(res)

class Tester(unittest.TestCase):
    def valid(self,actual,n):
        if len(actual)!=n: return False
        if 'aaa' in actual: return False
        if 'bbb' in actual: return False
        if 'ccc' in actual: return False
        return True
    def test1(self):
        a,b,c= 1,1,7
        Output= "ccaccbcc"
        actual = get_sol().longestDiverseString(a,b,c)
        print(Output,actual)
        self.assertEqual(True,Tester().valid(actual,len(Output)))
    def test2(self):
        a,b,c= 2,2,1
        Output= "aabbc"
        actual = get_sol().longestDiverseString(a,b,c)
        print(Output,actual)
        self.assertEqual(True,Tester().valid(actual,len(Output)))
    def test3(self):
        a,b,c= 7,1,0
        Output= "aabaa"
        actual = get_sol().longestDiverseString(a,b,c)
        print(Output,actual)
        self.assertEqual(True,Tester().valid(actual,len(Output)))
    def test4(self):
        a,b,c= 2,4,1
        Output= "bbaabbc"
        actual = get_sol().longestDiverseString(a,b,c)
        print(Output,actual)
        self.assertEqual(True,Tester().valid(actual,len(Output)))
    # def test5(self):
    # def test6(self):
    # def test7(self):
