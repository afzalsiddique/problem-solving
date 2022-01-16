import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
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