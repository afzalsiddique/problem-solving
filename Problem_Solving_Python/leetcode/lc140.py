# https://www.youtube.com/watch?v=WepWFGxiwRs
from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
# accepted
# don't understand why dp is slower? Ans: consider this case: ['aaaaaaaa'], ['a','aa','aaa','aaaa']
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def recur(i,path):
            if i==n:
                res.append(path)
                return path
            ret=[]
            for word in wordDict:
                length=len(word)
                if n-i<length: continue
                if s[i:i+length]==word:
                    ans = recur(i+length,path+[word])
                    for sub in ans:
                        ret.append(sub)
            return ret

        n=len(s)
        res=[]
        recur(0,[])
        return list(map(' '.join,res))
class Solution3: # AC. 32 ms
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        def helper(s,path):
            if len(s)==0:res.append(" ".join(path))
            n = len(s)
            for word in wordDict:
                w = len(word)
                if w>n:continue
                first,second = s[:w], s[w:]
                if first==word:
                    helper(second, path+[first])

        helper(s,[])
        return res

class Solution4: # AC. 100 ms
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        def word_break(s):
            if s in dp: return dp[s]
            result = []
            for word in wordDict:
                n = len(word)
                if s[:n] == word:
                    if n == len(s):
                        result.append(word)
                    else:
                        ans = word_break(s[len(word):])
                        for sub_ans in ans:
                            result.append(word + " " + sub_ans)
            dp[s] = result
            return result

        return word_break(s)


class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        def word_break(s):
            if s in dp: return dp[s]
            n = len(s)
            result = []
            for i in range(1, n + 1):
                word = s[:i]
                if word in wordDict:
                    if n == len(word):
                        result.append(word)
                    else:
                        tmp = word_break(s[i:])
                        for item in tmp:
                            result.append(word + " " + item)
            dp[s] = result
            return result

        return word_break(s)
class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(sorted(["cats and dog","cat sand dog"]), sorted(get_sol().wordBreak("catsanddog", ["cat","cats","and","sand","dog"])))
    def test02(self):
        s = "pineapplepenapple"
        wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
        self.assertEqual(sorted([ "pine apple pen apple", "pineapple pen apple", "pine applepen apple" ]), sorted(get_sol().wordBreak(s, wordDict)))
    def test_3(self):
        s = "applepineapple"
        wordDict = ["apple", "pine","pineapple"]
        actual = sorted(get_sol().wordBreak(s, wordDict))
        expected = sorted([ "apple pine apple", "apple pineapple" ])
        self.assertEqual(expected, actual)
    def test_4(self):
        s = "aaaaaaaaaa"
        wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa","aaaaaa"]
        actual = sorted(get_sol().wordBreak(s, wordDict))
        expected = ["jani na"]
        self.assertEqual(expected, actual)
    def test_5(self):
        s = "mycatsanddog"
        wordDict = ["cat", "cats", "and", "sand", "dog","my"]
        self.assertEqual(sorted(['my cat sand dog', 'my cats and dog']), sorted(get_sol().wordBreak(s, wordDict)))
