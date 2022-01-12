import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class TrieNode:
    def __init__(self, ch: Optional[str] = ''):
        self.ch = ch
        self.count = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children.keys():
                node.children[ch] = TrieNode(ch)
            node = node.children[ch]
        node.count += 1

    def search(self, word: str) -> int:
        def dfs(node: TrieNode, found: Optional[bool] = False) -> int:
            result = node.count*found
            for ch in word:
                if ch in node.children.keys():
                    result += dfs(node.children[ch], found or ch == word[0])
            return result
        return dfs(self.root)

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.add(word)
        return [trie.search(word) for word in puzzles]


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
