import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List, Optional; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=CUfWOQm-Nwc
    # https://leetcode.com/problems/parallel-courses-ii/discuss/1373540/Detailed-Explanations-%2B-Diagrams-%2B-Annotated-Code
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        def takeCourse(mask:int,i:int): return mask|(1<<i)
        def courseTaken(mask:int,i:int): return mask&(1<<i)
        @functools.lru_cache(None)
        def dfs(mask:int,inDegrees:tuple[int]):
            if mask==goal: return 0
            # when inDegree[i]==0, then it means all its prerequisite courses are taken
            nodes=[i for i in range(n) if not courseTaken(mask,i) and inDegrees[i]==0]
            ans=float('inf')
            minn=min(k,len(nodes)) # if there are not enough courses (k courses) available then we need to take all the courses available
            for kCourses in itertools.combinations(nodes,minn):
                newMask = mask
                newInDegrees=list(inDegrees)
                for course in kCourses:
                    newMask=takeCourse(newMask,course)
                    for nextCourse in g[course]:
                        newInDegrees[nextCourse]-=1 # one prerequisite of the next course is fulfilled
                    ans=min(ans,1+dfs(newMask,tuple(newInDegrees)))
            return ans

        inDegrees=[0]*n
        g=defaultdict(list)
        goal=(1<<n)-1
        for u,v in relations:
            u-=1; v-=1 # 0 based indexing
            g[u].append(v)
            inDegrees[v]+=1

        return dfs(0,tuple(inDegrees))


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(3, get_sol().minNumberOfSemesters(4, [[2,1],[3,1],[1,4]], 2))
    def test02(self):
        self.assertEqual(4, get_sol().minNumberOfSemesters(5,[[2,1],[3,1],[4,1],[1,5]],2))
    def test03(self):
        self.assertEqual(6, get_sol().minNumberOfSemesters(11,  [],2))
    # def test04(self):
