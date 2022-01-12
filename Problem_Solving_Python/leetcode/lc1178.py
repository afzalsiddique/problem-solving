import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/discuss/372145/Python-Bit-manipulation-detailed-explanation
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        def isOn(mask:int,i:int): return mask & (1<<i)
        def createMask(word):
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            return mask
        map=defaultdict(int)

        for w in words:
            map[createMask(w)]+=1

        res=[]

        for p in puzzles:
            mask = createMask(p)
            cnt=0
            sub=mask
            firstIdx=(ord(p[0])-ord('a'))
            while sub: # generate all submasks
                if isOn(sub,firstIdx):
                    cnt+=map[sub]
                sub = (sub-1) & mask # Kerninghan's theorm
            res.append(cnt)

        return res
class Solution2:
    # tle
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        def valid(puzzle:Counter,firstLetter:str,word:Counter):
            if word[firstLetter]<=0:
                return False
            for c in word:
                if puzzle[c]<=0:
                    return False
            return True
        def validAll(puzzle:Counter, firstLetter:str,words:List[Counter]):
            return sum(valid(puzzle,firstLetter,word) for word in words)

        firstLetters = [puzzle[0] for puzzle in puzzles]
        puzzles = [Counter(puzzle) for puzzle in puzzles]
        words = [Counter(word) for word in words]

        res=[]
        for i in range(len(puzzles)):
            res.append(validAll(puzzles[i],firstLetters[i],words))
        return res

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([1,1,3,2,4,0], get_sol().findNumOfValidWords(words = ["aaaa","asas","able","ability","actt","actor","access"], puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]))
    def test2(self):
        self.assertEqual([0,1,3,2,0], get_sol().findNumOfValidWords(words = ["apple","pleas","please"], puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]))
    # def test3(self):
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
