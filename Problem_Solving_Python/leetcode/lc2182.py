from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count=Counter(s)
        pq=[[-ord(x),x] for x in set(s)]
        heapify(pq)
        res=[]
        while len(res)<len(s):
            # print(res)
            _,c1=heappop(pq)
            if c1 not in count:
                continue
            if  count[c1]==0:
                count.pop(c1)
                continue
            if count[c1]<=repeatLimit:
                while count[c1]:
                    res.append(c1)
                    count[c1]-=1
                # print(c1)
                count.pop(c1)
            else:
                tmp=repeatLimit
                while tmp:
                    res.append(c1)
                    count[c1]-=1
                    tmp-=1
                while pq and count[pq[0][1]]==0:
                    heappop(pq)
                    # count[pq[0][1]]=0
                    # count.pop(pq[0][1])
                if pq and pq[0][1] in count and count[pq[0][1]]:
                    c2=pq[0][1]
                    res.append(c2)
                    count[c2]-=1
                    if count[c2]==0:
                        count.pop(c2)
                else:
                    break
                heappush(pq,[-ord(c1),c1])
        return ''.join(res)


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual("zzcccac", get_sol().repeatLimitedString("cczazcc",  3))
    def test02(self):
        self.assertEqual("bbabaa", get_sol().repeatLimitedString(s = "aababab", repeatLimit = 2))
    def test03(self):
        self.assertEqual("aa", get_sol().repeatLimitedString("aaaaaaaaaaa", 2))
    def test04(self):
        self.assertEqual("bbabbaa", get_sol().repeatLimitedString("aaaabbbb", 2))
    def test05(self):
        self.assertEqual("babababa", get_sol().repeatLimitedString("aaaabbbb", 1))
    def test06(self):
        self.assertEqual("zzzzyyyyxvvuuuuttssssssrqqqpponnmmmmmmlmmkjjiihhhhgggggfffeeeeddddccccbbbbbbab", get_sol().repeatLimitedString("mapzhptjmudmgdutgqcyscceybfzyqmmmmbdkgzssqnfyoxmebniribeubudsegsflsvhcgbhvzhjb", 6))
    def test07(self):
        self.assertEqual("mmlmb", get_sol().repeatLimitedString("mmmlb", 2))
    def test08(self):
        self.assertEqual("zyxyxwxwvwvuvuvututstrtrtqpqpqponononmlmkmkjigifiededededcbaba", get_sol().repeatLimitedString("xyutfpopdynbadwtvmxiemmusevduloxwvpkjioizvanetecnuqbqqdtrwrkgt", 1))
    def test09(self):
        self.assertEqual("qoq", get_sol().repeatLimitedString("oqqq", 1))
    def test10(self):
        a="mxiemm"
        e="xmimem"
        aa=get_sol().repeatLimitedString(a, 1)
        self.assertEqual(len(e),len(aa),'length not equal')
        self.assertEqual(e, aa)
    def test11(self):
        a="aabbcc"
        e="cbcba"
        aa=get_sol().repeatLimitedString(a, 1)
        self.assertEqual(len(e),len(aa),'length not equal')
        self.assertEqual(e, aa)
