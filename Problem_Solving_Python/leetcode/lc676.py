import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return MagicDictionary()
class MagicDictionary:
    # https://leetcode.com/problems/implement-magic-dictionary/discuss/107454/Python-without-*26-factor-in-complexity
    def __init__(self):
        self.di=defaultdict(set)
    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            for i in range(len(word)):
                tmp = word[:i]+'*'+word[i+1:]
                self.di[tmp].add(word)
        # print(self.di)
    def search(self, searchWord: str) -> bool:
        di = self.di
        for i in range(len(searchWord)):
            tmp = searchWord[:i]+'*'+searchWord[i+1:]
            if tmp in di:
                for src in di[tmp]:
                    if src!=searchWord:
                        return True
        return False
class MagicDictionary2:
    # slow
    def __init__(self):
        self.di=set()
    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.di.add(word)
    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            for letter in 'abcdefghijklmnopqrstuvwxyz':
                if searchWord[i]==letter: continue
                if searchWord[:i]+letter+searchWord[i+1:] in self.di: return True
        return False


class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = defaultdict(TrieNode)
class MagicDictionary3:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word):
        r = self.root
        for c in word:
            r = r.children[c]
        r.is_end = True

    def findWord(self, node, word, count):
        if count < 0: return False # early terminate
        if not word:
            return True if count == 0 and node.is_end else False
        for c, nxt in node.children.items():
            if word[0] == c:
                if self.findWord(nxt, word[1:], count):
                    return True
            else:
                if self.findWord(nxt, word[1:], count-1):
                    return True
        return False

    def buildDict(self, dict):
        for word in dict: self.addWord(word)
    def search(self, word):
        return self.findWord(self.root, word,1)

class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='MagicDictionary':
                obj = get_sol()
                outputs.append(None)
            elif cmd=='buildDict':
                outputs.append(obj.buildDict(input[0]))
            elif cmd=='search':
                outputs.append(obj.search(input[0]))
        return outputs
    def test_1(self):
        commands = ["MagicDictionary", "buildDict", "search", "search", "search", "search"]
        inputs=[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
        out_exptected = [None, None, False, True, False, False]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(out_exptected,outputs)