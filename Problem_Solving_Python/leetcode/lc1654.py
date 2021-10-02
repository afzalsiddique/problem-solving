import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution3()
class Solution:
    # https://leetcode.com/problems/minimum-jumps-to-reach-home/discuss/935419/Python-deque-BFS-O(max(x-max(forbidden))%2Ba%2Bb)
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        too_far=max([x]+forbidden) +a+b+1
        jumps=[float('inf')] * too_far
        jumps[0]=0
        for pos in forbidden: jumps[pos]=-1
        q = deque([0])
        while q:
            pos = q.popleft()
            if pos+a<too_far and jumps[pos+a]>jumps[pos]+1:
                q.append(pos+a)
                jumps[pos+a]=jumps[pos]+1
            if pos-b>0 and jumps[pos-b]>jumps[pos]+1:
                jumps[pos-b]=jumps[pos]+1
                if pos-b+a<too_far and jumps[pos-b+a]>jumps[pos-b]+2:
                    q.append(pos-b+a)
                    jumps[pos-b+a]=jumps[pos]+2
        return jumps[x] if jumps[x]<float('inf') else -1
class Solution2:
    # https://leetcode.com/problems/minimum-jumps-to-reach-home/discuss/935401/Python-DFS-(issue-with-121-test-case-solved)
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        toofar=max([x]+forbidden) +a+b+1
        forbidden = set(forbidden)
        minsofar = float('inf')

        position_cost = {}  # only record the cost when jumping forward
        def minjumps(cur_pos = 0, jumped_back = False, jumpsmade = 0):
            nonlocal minsofar, toofar
            if cur_pos < 0 or \
                    cur_pos in forbidden or \
                    cur_pos - b > toofar or \
                    minsofar > -1 and jumpsmade > minsofar: return

            if cur_pos == x:
                minsofar = min(minsofar, jumpsmade)
                return

            if jumped_back: # can only jump forward at this point
                minjumps(cur_pos + a, False, jumpsmade + 1)
                return
            elif cur_pos not in position_cost: position_cost[cur_pos] = jumpsmade
            elif jumpsmade >= position_cost[cur_pos]: return
            else: position_cost[cur_pos] = jumpsmade

            minjumps(cur_pos + a, False, jumpsmade + 1)
            minjumps(cur_pos - b, True, jumpsmade + 1)

        minjumps()
        if minsofar!=float('inf'): return minsofar
        return -1

class Solution3:
    # wrong ans
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden=set(forbidden)
        if x in forbidden: return -1
        def dfs(i, backward):
            if i in forbidden: return float('inf')
            if i>x+b: return float('inf')
            if i==x: return 0
            if i<0: return float('inf')
            if backward:
                return 1+min(dfs(i+a,True),dfs(i-b,False))
            else:
                return 1+dfs(i+a,True)

        ans= dfs(0,True)
        if ans==float('inf'): return -1
        return ans


class MyTestCase(unittest.TestCase):
    def test_1(self):
        forbidden = [14,4,18,1,15]; a = 3; b = 15; x = 9; Output= 3
        self.assertEqual(Output, get_sol().minimumJumps(forbidden,a,b,x))
    def test_2(self):
        forbidden = [8,3,16,6,12,20]; a = 15; b = 13; x = 11; Output= -1
        self.assertEqual(Output, get_sol().minimumJumps(forbidden,a,b,x))
    def test_3(self):
        forbidden = [1,6,2,14,5,17,4]; a = 16; b = 9; x = 7; Output= 2
        self.assertEqual(Output, get_sol().minimumJumps(forbidden,a,b,x))
    def test_4(self):
        forbidden =[]
        a=4
        b=5
        x=1
        Output = 7 # 0 -> 4 -> 8 -> 3 -> 7 -> 2 -> 6 -> 1.
        self.assertEqual(Output, get_sol().minimumJumps(forbidden,a,b,x))
    def test_5(self):
        forbidden= [162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98]
        a=29
        b=98
        x=80
        Output = 121
        self.assertEqual(Output, get_sol().minimumJumps(forbidden,a,b,x))
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):