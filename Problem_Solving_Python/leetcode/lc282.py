import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

class Solution:
    def addOperators(self, num: 'str', target: 'int') -> 'List[str]':
        res = []
        def backtracking(idx=0, path='', value=0, prev=None):
            if idx == len(num) and value == target:
                res.append(path)
                return
            for i in range(idx+1, len(num) + 1):
                tmp = int(num[idx: i])
                if prev is None : # no need to add '+','-','*'
                    backtracking(i, num[idx: i], tmp, tmp)
                else:
                    backtracking(i, path+'+'+num[idx: i], value + tmp, tmp)
                    backtracking(i, path+'-'+num[idx: i], value - tmp, -tmp)
                    # Imagine you are currently evaluating the expression 5 + 2 * 3, the dfs method has last = 2,
                    # cur= 7, To evaluate expression A + B * C, it should be read with multiplication taking
                    # precedence, A + (B * C), so result should be 5 + (2 * 3) => 11. Without last, one could end up
                    # calculating result as (5+2)*3 => 21 Hence the expression, cur - last + last * val => 7-2 + (2 *
                    # 3) = 11
                    backtracking(i, path+'*'+num[idx: i], value - prev + prev*tmp, prev*tmp)

                # deal with '025' case, string starts with '0'
                if num[idx] == '0':break

        backtracking()
        return res


class tester(unittest.TestCase):
    def test1(self):
        num = "123"
        target = 6
        Output= ["1*2*3","1+2+3"]
        self.assertEqual(Output,Solution().addOperators(num,target))
    def test2(self):
        num = "23"
        target = 6
        Output= ["2*3"]
        self.assertEqual(Output,Solution().addOperators(num,target))
    def test3(self):
        num = "105"
        target = 5
        Output= ["1*0+5","10-5"]
        self.assertEqual(Output,Solution().addOperators(num,target))
    def test4(self):
        num = "00"
        target = 0
        Output= ["0*0","0+0","0-0"]
        self.assertEqual(Output,Solution().addOperators(num,target))
    def test5(self):
        num = "3456237490"
        target = 9191
        Output= []
        self.assertEqual(Output,Solution().addOperators(num,target))
