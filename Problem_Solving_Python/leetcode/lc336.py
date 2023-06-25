from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # hashmap
    # https://www.youtube.com/watch?v=gys8p5fEkAg&t=322s
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPalindrome(word): return word==word[::-1]
        di = {word[::-1]:i for i,word in enumerate(words)}
        res=[]
        for i,word in enumerate(words):
            for length in range(len(word)+1):
                prefix = word[:length]
                suffix = word[length:]
                if isPalindrome(prefix) and suffix in di:
                    j = di[suffix]
                    if i!=j:
                        res.append([j,i])
                if suffix!="" and isPalindrome(suffix) and prefix in di:
                    j=di[prefix]
                    if i!=j:
                        res.append([i,j])
        return res
class TrieNode:
    def __init__(self):
        self.idx = -1 # similar to isEnd. index of the word which ends here
        self.pdromes_below = []
        self.children = defaultdict(TrieNode)
    def isEnding(self): return self.idx != -1 # is ending of some word

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def addInReverse(self, word, idx):
        node = self.root
        for i, letter in enumerate(reversed(word)): # add in reverse order
            remaining=word[:len(word)-i]
            if self.is_palindrome(remaining):
                node.pdromes_below.append(idx)
            node = node.children[letter]
        node.idx = idx
        return

    def search(self, word, idx):
        res=[]
        node = self.root
        for i, letter in enumerate(word):
            if node.isEnding() and idx != node.idx and self.is_palindrome(word[i:]):
                res.append([idx, node.idx])
            node = node.children.get(letter)
            if not node:
                return res
        for p in node.pdromes_below:
            if p != idx:
                res.append([idx, p])
        if node.isEnding() and idx != node.idx: # exact half palindrome. eg-> "abcd" and "dcba"
            res.append([idx, node.idx])
        return res

    def is_palindrome(self, w):
        i = 0
        j = len(w)-1
        while i < j:
            if w[i] != w[j]:
                return False
            i += 1
            j -= 1
        return True

class Solution2:
    # https://leetcode.com/problems/palindrome-pairs/discuss/79195/O(n-*-k2)-java-solution-with-Trie-structure/269808
    def palindromePairs(self, words:List[str])->List[List[str]]:
        res = []
        t = Trie()
        for idx, w in enumerate(words):
            t.addInReverse(w, idx)
        for idx, w in enumerate(words):
            res.extend(t.search(w, idx))
        return res


class Solution3:
    def palindromePairs(self, words):
        # https://leetcode.com/problems/palindrome-pairs/discuss/79209/Accepted-Python-Solution-With-Explanation
        lookup = {w:i for i,w in enumerate(words)}
        res = []
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                pre, suf = word[:j], word[j:]
                if pre==pre[::-1] and suf[::-1] != word and suf[::-1] in lookup:
                    res.append([lookup[suf[::-1]], i])
                if j != len(word) and suf==suf[::-1] and pre[::-1] != word and pre[::-1] in lookup:
                    res.append([i, lookup[pre[::-1]]])
        return res

# tle
class Solution2:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        m=len(words)
        res = []
        def palindrome(word):
            return word==word[::-1]

        for i in range(m):
            for j in range(i):
                if palindrome(words[j]+words[i]):
                    res.append([j,i])
        for i in reversed(range(m)):
            for j in reversed(range(i)):
                if palindrome(words[i]+words[j]):
                    res.append([i,j])
        return res

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(sorted([[0,1],[1,0],[3,2],[2,4]]),sorted(get_sol().palindromePairs(["abcd","dcba","lls","s","sssll"])))
    def test2(self):
        self.assertEqual(sorted([[0,1],[1,0]]),sorted(get_sol().palindromePairs(["bat","tab","cat"])))
    def test3(self):
        self.assertEqual(sorted([[0,1],[1,0]]),sorted(get_sol().palindromePairs(["a",""])))
    def test4(self):
        self.assertEqual(sorted([[1,0]]),sorted(get_sol().palindromePairs(["babsl","ls"])))
    def test5(self):
        self.assertEqual(sorted([[1,0]]),sorted(get_sol().palindromePairs(["abc","cb"])))
    def test6(self):
        self.assertEqual(sorted([[0,1]]),sorted(get_sol().palindromePairs(["abcb","a"])))
    def test7(self):
        self.assertEqual(sorted([[1,0],[0,2]]),sorted(get_sol().palindromePairs(["lls","s","sssll"])))
