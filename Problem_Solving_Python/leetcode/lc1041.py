import itertools
import math
import operator
import random
from bisect import *
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List



def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/robot-bounded-in-circle/discuss/290856/JavaC%2B%2BPython-Let-Chopper-Help-Explain
    def isRobotBounded(self, instructions):
        x, y, dx, dy = 0, 0, 0, 1
        for i in instructions:
            if i == 'R': dx, dy = dy, -dx
            if i == 'L': dx, dy = -dy, dx
            if i == 'G': x, y = x + dx, y + dy
        return (x, y) == (0, 0) or (dx, dy) != (0,1)

class Solution2:
    def isRobotBounded(self, instructions):
        x, y, dx, dy = 0, 0, 0, 1
        for _ in range(4):
            for i in instructions:
                if i == 'R': dx, dy = dy, -dx
                if i == 'L': dx, dy = -dy, dx
                if i == 'G': x, y = x + dx, y + dy
            if (x,y) == (0,0): return True
        return False
class Solution3:
    def isRobotBounded(self, instructions):
        north=(0,1)
        x, y, dx, dy = 0, 0, 0, 1
        for _ in range(4):
            for i in instructions:
                if i == 'R': dx, dy = dy, -dx
                if i == 'L': dx, dy = -dy, dx
                if i == 'G': x, y = x + dx, y + dy
            if (x,y) == (0,0) and (dx,dy)==north: return True
        return False
class Solution4:
    def isRobotBounded(self, instructions: str) -> bool:
        def change_dir(cur_dir,rotation):
            di={(0,1):'N',(-1,0):'W',(1,0):'E',(0,-1):'S'}
            di2={'N':(0,1),'W':(-1,0),'E':(1,0),'S':(0,-1)}
            cur_dir = di[cur_dir]
            right='ESWNE'
            left='ENWSE'
            if rotation=='R':
                idx =right.index(cur_dir)+1
                cur_dir = right[idx].upper()
            else:
                idx = left.index(cur_dir)+1
                cur_dir = left[idx].upper()
            cur_dir = di2[cur_dir]
            return cur_dir

        dir=(0,1)
        initial= [0,0]
        cur = [0,0]
        for _ in range(4):
            for cmd in instructions:
                if cmd=='G':
                    cur[0]+=dir[0]
                    cur[1]+=dir[1]
                else: dir = change_dir(dir,cmd)
            if cur==initial: return True
        return False

        # also works
        dir=(0,1)
        initial_dir=(0,1)
        initial= [0,0]
        cur = [0,0]
        for _ in range(4):
            for cmd in instructions:
                if cmd=='G':
                    cur[0]+=dir[0]
                    cur[1]+=dir[1]
                else:
                    dir = change_dir(dir,cmd)
            if cur==initial and dir==initial_dir: return True
        return False
class mytestcase(unittest.TestCase):
    def test01(self):
        instructions = "GGLLGG"
        Output= True
        self.assertEqual(Output,get_sol().isRobotBounded(instructions))
    def test02(self):
        instructions = "GG"
        Output= False
        self.assertEqual(Output,get_sol().isRobotBounded(instructions))
    def test03(self):
        instructions = "GL"
        Output= True
        self.assertEqual(Output,get_sol().isRobotBounded(instructions))
    def test04(self):
        instructions = "RRGRRGLLLRLGGLGLLGRLRLGLRLRRGLGGLLRRRLRLRLLGRGLGRRRGRLG"
        Output= False
        self.assertEqual(Output,get_sol().isRobotBounded(instructions))
