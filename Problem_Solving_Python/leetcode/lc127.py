# https://leetcode.com/problems/word-ladder/
# https://www.youtube.com/watch?v=ZVJ3asMoZ18
# https://leetcode.com/problems/word-ladder/discuss/40729/Compact-Python-solution
from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        myset = set(wordList)
        if endWord not in myset:
            return 0

        q = deque()
        q.append(beginWord)
        depth = 0
        while q:
            depth+=1
            level_size = len(q) # no of elements at a level
            for _ in range(level_size):
                curr = q.popleft()
                # check for all possible level 1 words
                for i in range(len(curr)): # for each index
                    for c in "abcdefghijklmnopqrstuvwxyz": # try all possible chars
                        temp = curr[:i] + c + curr[i+1:]
                        if curr == temp: # skip the same word
                            continue
                        if temp == endWord:
                            return depth+1 # endword found
                        if temp in myset:
                            q.append(temp)
                            myset.remove(temp)
        return 0
