from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # backtrack
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def takeWord(i:int):
            valid=True
            for c in words[i]:
                if letters[c]==0:
                    valid=False
                letters[c]-=1
            return valid
        def reverseTakeWord(i:int):
            for c in words[i]:
                letters[c]+=1
        def calScore(i:int):
            res=0
            for c in words[i]:
                idx=ord(c)-ord('a')
                res+=score[idx]
            return res
        def backtrack(start: int):
            res=0
            for i in range(start,n):
                valid=takeWord(i)
                if valid:
                    res=max(res,calScore(i)+backtrack(i + 1))
                reverseTakeWord(i)
            return res

        n=len(words)
        letters=Counter(letters)
        return backtrack(0)
class Solution3:
    # dp
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def wordCanBeFormed(i, lettersLeft:List[str]):
            for c in words[i]:
                if c not in lettersLeft:
                    return False
                lettersLeft.remove(c)
            return True
        def formWord(i, lettersLeft:List[str]):
            for c in words[i]:
                lettersLeft.remove(c)
            return lettersLeft
        def calculateScore(i):
            total=0
            for c in words[i]:
                i=ord(c)-ord('a')
                total+=score[i]
            return total

        @cache
        def dp(i, lettersLeft:tuple):
            if i==n:
                return 0
            res=0
            for j in range(i,n):
                if wordCanBeFormed(j, list(lettersLeft)):
                    li=formWord(j, list(lettersLeft))
                    score1=calculateScore(j)
                    score2=dp(j+1,tuple(li))
                    res=max(res,score1+score2)
            return res

        n=len(words)
        return dp(0,tuple(sorted(letters)))
class Solution4:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def is_on(mask,i): return (mask>>i)&1 # returns 1 when True or 0 when False
        def toIdx(c): return ord(c)-ord('a') # ['a'->0, 'b'->1]
        def iterableToListOfInt(s): return list(map(toIdx,s)) # {'abc'->[0,1,2],  '['b','c','d']->[1,2,3] }
        def countLetters(mask):
            count=Counter()
            for i in range(n):
                if is_on(mask,i):
                    tmpCount=Counter(words[i])
                    count+=tmpCount
            return count
        def enoughLetter(count):
            return all(letterCnt[i]>=count[i] for i in range(26))
        def calcPoints(mask):
            res=0
            for i in range(n):
                if is_on(mask,i):
                    for ch in words[i]:
                        res+=score[ch]
            return res


        letters = list(iterableToListOfInt(letters))
        words = list(map(iterableToListOfInt,words))
        letterCnt=Counter(letters)
        n=len(words)
        res=0
        for mask in range(1<<n):
            count = countLetters(mask)
            if enoughLetter(count):
                res=max(res,calcPoints(mask))
        return res
class Solution2:
    # tle
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def wordCanBeTaken(word:Counter, letters:Counter):
            for c in word:
                if letters[c]<word[c]:
                    return False
            return True
        def newLetters(word:Counter, letters:Counter):
            return letters - word
        def calScore(word:Counter):
            res=0
            for c in word:
                idx=ord(c)-ord('a')
                res+=score[idx]*word[c]
            return res
        def backtrack(words:List[Counter], letters:Counter):
            res=0
            for i in range(len(words)):
                word=words[i]
                if wordCanBeTaken(word, letters):
                    res=max(res, calScore(word) + backtrack(words[:i] +words[i+1:], newLetters(word, letters)))
            return res

        words=[Counter(w) for w in words]
        letters=Counter(letters)
        return backtrack(words,letters)
class Solution3:
    # wrong
    # greedy
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def getBestWord(words:List[Counter],letters:Counter):
            idx=-1
            maxScore=0
            for i in range(len(words)):
                word=words[i]
                if wordCanBeTaken(word,letters):
                    tmp=calScore(word)
                    if tmp>maxScore:
                        maxScore=tmp
                        idx=i
            return idx

        def wordCanBeTaken(word:Counter, letters:Counter):
            for c in word:
                if letters[c]<word[c]:
                    return False
            return True
        def newLetters(word:Counter, letters:Counter):
            return letters - word
        def calScore(word:Counter):
            res=0
            for c in word:
                idx=ord(c)-ord('a')
                res+=score[idx]*word[c]
            return res
        def recur(words:List[Counter], letters:Counter):
            res=0
            i=getBestWord(words,letters)
            if i==-1: return res
            res=calScore(words[i]) + recur(words[:i] +words[i+1:], newLetters(words[i], letters))
            return res

        words=[Counter(w) for w in words]
        letters=Counter(letters)
        return recur(words,letters)

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(23,get_sol().maxScoreWords(["dad","good","dog"], ["a","a","c","d","d","d","g","o","o"], [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]))
    def test02(self):
        self.assertEqual(23,get_sol().maxScoreWords(["dog","cat","dad","good"],["a","a","c","d","d","d","g","o","o"], [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]))
    def test03(self):
        self.assertEqual(27,get_sol().maxScoreWords(["xxxz","ax","bx","cx"], ["z","a","b","c","x","x","x"], [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]))
    def test04(self):
        self.assertEqual(0,get_sol().maxScoreWords(["leetcode"], ["l","e","t","c","o","d"], [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]))
    def test05(self):
        self.assertEqual(298,get_sol().maxScoreWords(["daeagfh","acchggghfg","feggd","fhdch","dbgadcchfg","b","db","fgchfe","baaedddc"], ["a","a","a","a","a","a","a","b","b","b","b","b","b","b","b","b","c","c","c","c","c","c","c","c","c","c","c","d","d","d","d","d","d","d","d","d","d","d","d","d","d","e","e","e","e","e","e","e","e","e","e","f","f","f","f","f","f","f","f","f","f","f","f","f","f","g","g","g","g","g","g","g","g","g","g","g","g","h","h","h","h","h","h","h","h","h","h","h","h","h"], [2,1,9,2,10,5,7,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
    # def test06(self):
    # def test07(self):
    # def test08(self):
