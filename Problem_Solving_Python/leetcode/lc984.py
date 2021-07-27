import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/string-without-aaa-or-bbb/discuss/226740/Clean-C%2B%2Bpython-solution
    def strWithout3a3b(self, a: int, b: int) -> str:
        c1,c2='a','b'
        def h(cnt1, cnt2, c1, c2):
            if cnt2>cnt1: return h(cnt2, cnt1, c2, c1)
            elif cnt1==cnt2: return (c1 + c2) * cnt1
            elif cnt2==0: return c1 * cnt1
            else: return c1 + c1 + c2 + h(cnt1 - 2, cnt2 - 1, c1, c2)

        return h(a,b,c1,c2)
class Solution2:
    # https://leetcode.com/problems/string-without-aaa-or-bbb/discuss/226740/Clean-C%2B%2Bpython-solution
    def strWithout3a3b(self, a: int, b: int) -> str:
        def h(a,b):
            if a==0: return 'b'*b
            elif b==0: return 'a'*a
            elif a==b: return 'ab'*a
            elif a>b: return 'aab' + h(a-2,b-1)
            elif b>a: return 'bba' + h(a-1,b-2)

        return h(a,b)

class Solution3:
    # https://leetcode.com/problems/string-without-aaa-or-bbb/discuss/508543/APPLES-and-BANANAS-solution-(with-picture)
    def strWithout3a3b(self, a: int, b: int) -> str:
        ch1,ch2='a','b'
        freq1,freq2=a,b
        def h(freq1, freq2,ch1,ch2):
            if freq2>freq1: return h(freq2,freq1,ch2,ch1)
            max_rows = math.ceil(freq1/2)
            res = [[] for _ in range(max_rows)]
            i=0
            while freq1:
                res[i].append(ch1)
                freq1-=1
                if freq1:
                    res[i].append(ch1)
                    freq1-=1
                i+=1

            i=0
            while freq2:
                res[i].append(ch2)
                freq2-=1
                i+=1
                i%=max_rows
            return res

        res=h(freq1,freq2,ch1,ch2)
        for i in range(len(res)):
            res[i]=''.join(res[i])
        res=''.join(res)
        return res


def valid(actual:str):
    x=actual.find('aaa')
    y=actual.find('bbb')
    return x==y==-1
class tester(unittest.TestCase):
    def test1(self):
        a = 1; b = 2
        actual =get_sol().strWithout3a3b(a,b)
        print(actual)
        self.assertEqual(True,valid(actual))
    def test2(self):
        a = 4; b = 1
        actual =get_sol().strWithout3a3b(a,b)
        print(actual)
        self.assertEqual(True,valid(actual))
    def test3(self):
        a,b=4,4
        actual =get_sol().strWithout3a3b(a,b)
        print(actual)
        self.assertEqual(True,valid(actual))
    def test4(self):
        a,b=5,6
        actual =get_sol().strWithout3a3b(a,b)
        print(actual)
        self.assertEqual(True,valid(actual))
    def test5(self):
        a,b=6,5
        actual =get_sol().strWithout3a3b(a,b)
        print(actual)
        self.assertEqual(True,valid(actual))
    def test6(self):
        a,b= 4, 1
        actual =get_sol().strWithout3a3b(a,b)
        print(actual)
        self.assertEqual(True,valid(actual))
    def test7(self):
        a,b= 1,3
        actual =get_sol().strWithout3a3b(a,b)
        print(actual)
        self.assertEqual(True,valid(actual))
    def test8(self):
        a,b= 2,5
        actual =get_sol().strWithout3a3b(a,b)
        print(actual)
        self.assertEqual(True,valid(actual))
