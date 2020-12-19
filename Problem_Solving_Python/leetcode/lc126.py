# https://leetcode.com/problems/word-ladder-ii/discuss/40482/Python-simple-BFS-layer-by-layer/322524
import collections
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        wordSet = set(wordList)  # faster checks against dictionary
        layer = {}
        layer[beginWord] = [[beginWord]]  # stores current word and all possible sequences how we got to it

        while layer:
            newlayer = collections.defaultdict(list)  # returns [] on missing keys, just to simplify code
            for word in layer:
                if word == endWord:
                    return layer[word]  # return all found sequences
                for i in range(len(word)):  # change every possible letter and check if it's in dictionary
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + c + word[i + 1:]
                        if newWord in wordSet:
                            newlayer[newWord] += [j + [newWord] for j in layer[
                                word]]  # add new word to all sequences and form new layer element
            wordSet -= set(newlayer.keys())  # remove from dictionary to prevent loops
            layer = newlayer  # move down to new layer

        return []