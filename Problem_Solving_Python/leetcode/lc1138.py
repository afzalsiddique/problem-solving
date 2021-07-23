import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        def manhattan(x1,y1,x2,y2):
            return (x2-x1,y2-y1)
        di={}
        string = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(26):
            di[string[i]] = (i//5,i%5)
        x,y=0,0
        res=[]
        for ch in target:
            x2,y2=di[ch]
            if ch!='z' and (x,y)==(5,0):
                x-=1
                res.append('U')
            dx,dy=manhattan(x,y,x2,y2)
            if dy>0:
                res.append('R'*dy)
            else:
                res.append('L'*abs(dy))
            if dx>0:
                res.append('D'*dx)
            else:
                res.append('U'*abs(dx))
            res.append('!')
            x,y=di[ch]
        return ''.join(res)


class MyTestCase(unittest.TestCase):
    # tests don't work although code is perfect
    def test_1(self):
        self.assertEqual("DDR!UURRR!!DDD!", get_sol().alphabetBoardPath('leet'))
    def test_2(self):
        self.assertEqual("RR!DDRR!UUL!R!", get_sol().alphabetBoardPath('code'))
    def test_3(self):
        self.assertEqual("DDDDD!UUUUURRR!DDDDLLLD!", get_sol().alphabetBoardPath('zdz'))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
