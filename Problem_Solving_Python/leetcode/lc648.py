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
            # if root found return the root
            # else return the original word
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
class Solution2:
    # leetcode solution
    # time O(sum of len(word)^2 for every word)
    # space O(len(sentence)
    def replaceWords(self, roots, sentence):
        rootset = set(roots)

        def replace(word):
            for i in range(1,len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word

        return " ".join(map(replace, sentence.split()))
class Solution3:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=lambda x:len(x))
        sentence=sentence.split()
        for word1 in dictionary:
            for i,word2 in enumerate(sentence):
                if len(word1)>len(word2): continue
                if word1==word2[:len(word1)]:
                    sentence[i]=word1
        return ' '.join(sentence)
class tester(unittest.TestCase):
    def test1(self):
        dictionary = ["ac","ab"]
        sentence = "it is abnormal that this solution is accepted"
        Output= "it is ab that this solution is ac"
        self.assertEqual(Output,get_sol().replaceWords(dictionary,sentence))
    def test2(self):
        dictionary = ["cat","bat","rat"]
        sentence = "the cattle was rattled by the battery"
        Output= "the cat was rat by the bat"
        self.assertEqual(Output,get_sol().replaceWords(dictionary,sentence))
    def test3(self):
        dictionary = ["a", "aa", "aaa", "aaaa"]
        sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
        Output= "a a a a a a a a bbb baba a"
        self.assertEqual(Output,get_sol().replaceWords(dictionary,sentence))
    def test4(self):
        dictionary = ["catt","cat","bat","rat"]
        sentence = "the cattle was rattled by the battery"
        Output= "the cat was rat by the bat"
        self.assertEqual(Output,get_sol().replaceWords(dictionary,sentence))
    def test5(self):
        dictionary = ["a","b","c"]
        sentence = "aadsfasf absbs bbab cadsfafs"
        Output= "a a b c"
        self.assertEqual(Output,get_sol().replaceWords(dictionary,sentence))
