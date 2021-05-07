import math
import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
def get_sol(): return Solution()

class Solution:
    # bi-directional bfs
    # https://leetcode.com/problems/open-the-lock/discuss/110237/Regular-java-BFS-solution-and-2-end-BFS-solution-with-improvement
    def openLock(self, deadends: List[str], target: str) -> int:
        begin=set()
        end = set()
        vis = set(deadends)
        begin.add('0000')
        end.add(target)
        level = -1
        while begin and end:
            if len(begin)>len(end):
                begin,end=end,begin
            level+=1
            temp=set()
            for s in begin:
                if s in end: return level
                if s in vis: continue
                vis.add(s)
                for i in range(4):
                    s1=list(s)
                    s2=list(s)
                    c = s[i]
                    s1[i]=str(int(c)+1) if c!='9' else '0'
                    s2[i]=str(int(c)-1) if c!='0' else '9'
                    s1 = ''.join(s1)
                    s2 = ''.join(s2)
                    if s1 not in vis: temp.add(s1)
                    if s2 not in vis: temp.add(s2)
            begin=temp
        return -1
class Solution2:
    # bfs
    def openLock(self, deadends: List[str], target: str) -> int:
        def get_successor(src):
            res=[]
            for i in range(len(src)):
                num = int(src[i])
                res.append(src[:i] + str((num + 1) % 10) + src[i + 1:])
                res.append(src[:i] + str((num - 1) % 10) + src[i + 1:])
            return res
        vis,depth=set(deadends),-1
        q=deque(['0000'])
        while q:
            depth+=1
            for _ in range(len(q)):
                cur =q.popleft()
                if cur==target: return depth
                if cur in vis: continue
                vis.add(cur)
                q.extend(get_successor(cur))
        return -1
