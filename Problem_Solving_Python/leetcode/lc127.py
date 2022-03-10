from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()

# https://www.youtube.com/watch?v=ZVJ3asMoZ18

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def getNeighbors(word:str,i:int): # ('hit',0) -> ['ait','bit','cit',...]
            li=[]
            for c in string.ascii_lowercase:
                newWord=word[:i]+c+word[i+1:]
                if newWord in wordList:
                    wordList.remove(newWord)
                    li.append(newWord)
            return li
        def getAllNeighbours(word):
            li=[]
            for i in range(len(word)):
                li.extend(getNeighbors(word,i))
            return li

        q=deque([beginWord])
        wordList=set(wordList)
        if endWord not in wordList: return 0
        res=1
        while q:
            for _ in range(len(q)):
                word=q.popleft()
                if word==endWord:
                    return res
                q.extend(getAllNeighbours(word))
            res+=1
        return 0
class Solution2:
    # https://leetcode.com/problems/word-ladder/discuss/40729/Compact-Python-solution
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        myset = set(wordList)
        if endWord not in myset:
            return 0

        q = deque()
        q.append(beginWord)
        depth = 0
        while q:
            depth+=1
            for _ in range(len(q)):
                curr = q.popleft()
                # check for all possible level 1 words
                for i in range(len(curr)): # for each index
                    for c in "abcdefghijklmnopqrstuvwxyz": # try all possible chars
                        temp = curr[:i] + c + curr[i+1:]
                        if curr == temp: # skip the same word
                            continue
                        if temp == endWord:
                            return depth+1 # endword found
                        if temp in myset:
                            q.append(temp)
                            myset.remove(temp)
        return 0
class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(5, get_sol().ladderLength( "hit", "cog", ["hot","dot","dog","lot","log","cog"]))
    def test02(self):
        self.assertEqual(0, get_sol().ladderLength( "hit", "cog", ["hot","dot","dog","lot","log"]))
    def test03(self):
        self.assertEqual(0, get_sol().ladderLength("hot", "dog", ["hot","dog"]))
    def test04(self):
        self.assertEqual(0, get_sol().ladderLength("hit", "cog", ["hot","dot","tog","cog"]))
    def test05(self):
        self.assertEqual(4, get_sol().ladderLength("teach", "place", ["peale","wilts","place","fetch","purer","pooch","peace","poach","berra","teach","rheum","peach"]))
