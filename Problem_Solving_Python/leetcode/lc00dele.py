import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class Solution:
    # time O(len(sentence))
    # space O(len(sentence))
    class Node:
        def __init__(self):
            self.is_word=False
            self.children={}
        def __repr__(self): return str(self.children)
    class Trie:
        def __init__(self):
            self.root=Solution.Node()
        def __repr__(self): return str(self.root)
        def insert(self,word):
            node = self.root
            for c in word:
                if c not in node.children:
                    node.children[c]=Solution.Node()
                node=node.children[c]
            node.is_word=True
        def find_prefix(self,word):
            path=[]
            node=self.root
            for c in word:
                if node.is_word: return ''.join(path)
                if c not in node.children: return word
                path.append(c)
                node=node.children[c]
            return word
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie=Solution.Trie()
        for root in dictionary:
            trie.insert(root)
        sentence=sentence.split()
        for i in range(len(sentence)):
            sentence[i] = trie.find_prefix(sentence[i])
        return ' '.join(sentence)
class tester(unittest.TestCase):
    def test1(self):
        dictionary = ["cat","bat","rat"]
        sentence = "the cattle was rattled by the battery"
        Output= "the cat was rat by the bat"
        self.assertEqual(Output,Solution().replaceWords(dictionary,sentence))
    def test2(self):
        dictionary = ["ac","ab"]
        sentence = "it is abnormal that this solution is accepted"
        Output= "it is ab that this solution is ac"
        self.assertEqual(Output,Solution().replaceWords(dictionary,sentence))
    def test3(self):
        dictionary = ["a", "aa", "aaa", "aaaa"]
        sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
        Output= "a a a a a a a a bbb baba a"
        self.assertEqual(Output,Solution().replaceWords(dictionary,sentence))
    def test4(self):
        dictionary = ["catt","cat","bat","rat"]
        sentence = "the cattle was rattled by the battery"
        Output= "the cat was rat by the bat"
        self.assertEqual(Output,Solution().replaceWords(dictionary,sentence))
    def test5(self):
        dictionary = ["a","b","c"]
        sentence = "aadsfasf absbs bbab cadsfafs"
        Output= "a a b c"
        self.assertEqual(Output,Solution().replaceWords(dictionary,sentence))
