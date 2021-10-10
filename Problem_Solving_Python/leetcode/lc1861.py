import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        STONE,OBSTACLE,EMPTY='#','*','.'
        m,n=len(box),len(box[0])
        res = [[EMPTY]*m for _ in range(n)]
        for i in range(m):
            j=n-1
            while j>=0:
                tmp_j=j
                cnt=0
                while tmp_j>=0 and box[i][tmp_j]!=OBSTACLE:
                    if box[i][tmp_j]==STONE:
                        box[i][tmp_j]=EMPTY
                        cnt+=1
                    tmp_j-=1
                while j!=tmp_j:
                    if cnt:
                        box[i][j]=STONE
                        cnt-=1
                    j-=1
                j-=1

        for i in range(m):
            for j in range(n):
                res[j][m-1-i]=box[i][j]
        return res


class MyTestCase(unittest.TestCase):
    def test1(self):
        box = [["#",".","#"]]
        Output= [["."],
                 ["#"],
                 ["#"]]
        self.assertEqual(Output, get_sol().rotateTheBox(box))
    def test2(self):
        box = [["#",".","*","."],
              ["#","#","*","."]]
        Output= [["#","."],
                 ["#","#"],
                 ["*","*"],
                 [".","."]]
        self.assertEqual(Output, get_sol().rotateTheBox(box))
    def test3(self):
        box = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
        Output= [[".","#","#"],
                 [".","#","#"],
                 ["#","#","*"],
                 ["#","*","."],
                 ["#",".","*"],
                 ["#",".","."]]
        self.assertEqual(Output, get_sol().rotateTheBox(box))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
