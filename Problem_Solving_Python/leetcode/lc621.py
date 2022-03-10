from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/task-scheduler/discuss/104501/Java-PriorityQueue-solution-Similar-problem-Rearrange-string-K-distance-apart/902800
    # time O(nlogn) space O(26)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        pq=[[-count[x],x] for x in count] # [-count,task]
        heapify(pq)
        res=0
        while pq:
            tmp=[]
            interval=n+1
            while interval and pq:
                _,task=heappop(pq)
                count[task]-=1
                tmp.append(task)
                res+=1
                interval-=1
            for t in tmp:
                if count[t]:
                    heappush(pq,[-count[t],t])
            if not pq:
                break
            res+=interval
        return res
class Solution2:
    # https://leetcode.com/problems/task-scheduler/discuss/104500/Java-O(n)-time-O(1)-space-1-pass-no-sorting-solution-with-detailed-explanation
    # time O(n) space O(1)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        maxx=max(count.values())
        maxCount=sum(1 for x in count if count[x]==maxx)

        partCount = maxx - 1
        partLength = n - (maxCount - 1)
        emptySlots = partCount * partLength # empty slots after filling with all the most frequent tasks
        tasksRemaining = len(tasks) - maxx * maxCount # tasks remaining after filling all the most frequent tasks
        idles = max(0,emptySlots-tasksRemaining)
        return len(tasks)+idles
class Solution3:
    # https://www.youtube.com/watch?v=tGw5GbDekTU
    def leastInterval(self, tasks, n):
        curr_time, di = 0, defaultdict(int)
        for t in tasks: di[t]+=1
        pq = []
        for v in di.values(): heappush(pq, -1*v)
        while pq:
            li = []
            for _ in range(n+1):
                curr_time += 1
                if pq:
                    x = heappop(pq) * (-1)
                    if x != 1: # not finished
                        li.append(x-1)
                if not pq and not li:
                    break
            for val in li:
                heappush(pq, -val)
        return curr_time

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(7,get_sol().leastInterval(["A","A","B","B","C","C"], 3))
    def test02(self):
        self.assertEqual(6,get_sol().leastInterval(["A","A","A","B","B","B"], 0))
    def test03(self):
        self.assertEqual(16,get_sol().leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))
    def test04(self):
        self.assertEqual(8,get_sol().leastInterval(["A","A","A","B","B","B"], 2))
    def test05(self):
        self.assertEqual(10,get_sol().leastInterval(["A","B","C","D","E","A","B","C","D","E"], 4))