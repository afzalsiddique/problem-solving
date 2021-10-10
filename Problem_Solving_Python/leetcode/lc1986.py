import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        def turnOn(jobs,job):
            return jobs | (1<<job)
        def isSelected(jobs,job):
            return (jobs & (1<<job))
        def allSelected(tasks):
            return tasks == ((1<<n)-1)

        @lru_cache(None)
        def backtrack(state,remainTime):
            if allSelected(state): return 0
            ans = n
            for i in range(n):
                if not isSelected(state,i):
                    new_state = turnOn(state,i)
                    if tasks[i] <= remainTime:
                        ans = min(ans, backtrack(new_state, remainTime - tasks[i]))  # Consume current session
                    else:
                        ans = min(ans, backtrack(new_state, sessionTime - tasks[i]) + 1)  # Create new session

            return ans

        n=len(tasks)
        return backtrack(0,sessionTime) + 1

class MyTestCase(unittest.TestCase):
    def test1(self):
        tasks,sessionTime = [1,2,3],  3
        Output= 2
        self.assertEqual(Output, get_sol().minSessions(tasks,sessionTime))
    def test2(self):
        tasks,sessionTime = [3,1,3,1,1],  8
        Output= 2
        self.assertEqual(Output, get_sol().minSessions(tasks,sessionTime))
    def test3(self):
        tasks,sessionTime = [1,2,3,4,5],  15
        Output= 1
        self.assertEqual(Output, get_sol().minSessions(tasks,sessionTime))
    def test4(self):
        tasks,sessionTime = [5,7,5], 7
        Output= 3
        self.assertEqual(Output, get_sol().minSessions(tasks,sessionTime))
    def test5(self):
        tasks,sessionTime = [1,5,7,10,3,8,4,2,6,2], 10
        Output= 5
        self.assertEqual(Output, get_sol().minSessions(tasks,sessionTime))
    # def test6(self):
