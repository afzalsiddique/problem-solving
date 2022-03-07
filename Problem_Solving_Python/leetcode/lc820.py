import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    class TrieNode:
        def __init__(self):
            self.children={}
        def __repr__(self): return str(self.children)
    class Trie:
        def __init__(self):
            self.root=Solution.TrieNode()
        def insert_reverse(self, word):
            word = word[::-1]
            node = self.root
            for ch in word:
                if ch not in node.children:
                    node.children[ch]=Solution.TrieNode()
                node=node.children[ch]

    def minimumLengthEncoding(self, words: List[str]) -> int:
        self.length=0
        def dfs(depth,root:Solution.TrieNode):
            if not root: return
            if not len(root.children):
                self.length+=depth+1 # "+1" for "#"
            for child_node in root.children.values():
                dfs(depth+1,child_node)


        trie = Solution.Trie()
        for word in words:
            trie.insert_reverse(word)

        dfs(0,trie.root)
        return self.length
class Solution2:
    # https://leetcode.com/problems/short-encoding-of-words/discuss/125811/C%2B%2BJavaPython-Easy-Understood-Solution-with-Explanation
    # time O(nk^2)
    # space O(nk)
    # hashset only works because 1<=k<=7. must use trie when k is large
    def minimumLengthEncoding(self, words: List[str]) -> int:
        sett=set(words)
        for word in words:
            for i in range(1,len(word)):
                suffix=word[i:]
                sett.discard(suffix)
        return sum(len(word) for word in sett) + len(sett)
class Solution3:
    # time O(knlogn)
    # space O(nk^2)
    # hashset only works because 1<=k<=7. must use trie when k is large
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = sorted(words,key=len,reverse=True)
        sett=set()
        lengths=[] # length of chosen words
        cnt=0
        for word in words:
            if word not in sett:
                lengths.append(len(word))
                cnt+=1
            else:
                continue
            for i in range(len(word)):
                suffix = word[i:]
                # print(suffix)
                sett.add(suffix)
        return sum(lengths)+cnt


class Tester(unittest.TestCase):
    def test01(self):
        words = ["time", "me", "bell"]
        Output= 10
        self.assertEqual(Output,get_sol().minimumLengthEncoding(words))
    def test02(self):
        words = ["t"]
        Output= 2
        self.assertEqual(Output,get_sol().minimumLengthEncoding(words))
    def test03(self):
        words = ["ctxdic","c"]
        Output= 7
        self.assertEqual(Output,get_sol().minimumLengthEncoding(words))

    # def test04(self):
    # def test05(self):
