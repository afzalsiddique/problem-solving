from bisect import bisect_left
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List



class Solution:
    # https://www.youtube.com/watch?v=khddrw6Bfyw
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort()
        n = len(people)
        res = [[-1,None] for _ in range(n)]
        for my_h,my_f in people:
            cnt = my_f
            for i in range(n):
                h = res[i][0]
                if not cnt and h==-1:
                    res[i] = [my_h,my_f]
                    break
                if h>=my_h or h==-1:
                    cnt-=1
        return res

class mycase(unittest.TestCase):
    def test1(self):
        self.assertEqual([[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]],Solution().reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
    def test2(self):
        self.assertEqual([[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]],Solution().reconstructQueue([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]))
