from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union, Dict; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list, ListNode
from Problem_Solving_Python.template.binary_tree import deserialize,serialize

def get_sol(): return Solution()
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetingCount=defaultdict(int)

        rooms=[] # pq -> (room_no)
        for room_no in range(n):
            heappush(rooms,room_no)

        upcoming=[] # pq -> (start,end)
        for a,b in meetings:
            heappush(upcoming,[a,b])

        ongoing=[] # pq -> (end,room_no)

        while upcoming:
            next_meeting_start,next_meeting_end=heappop(upcoming)
            while ongoing and ongoing[0][0]<=next_meeting_start: # update empty rooms before next meeting
                _,room=heappop(ongoing)
                heappush(rooms,room)
            if rooms: # empty rooms available
                room=heappop(rooms)
                meetingCount[room]+=1
            else:
                last_meeting_end,room=heappop(ongoing)
                meetingCount[room]+=1
                delay=last_meeting_end-next_meeting_start
                next_meeting_end+=delay
            heappush(ongoing,[next_meeting_end,room])
        return max(meetingCount,key=lambda x:(meetingCount[x],-x))


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(0, get_sol().mostBooked(2, [[0,10],[1,5],[2,7],[3,4]]))
    def test02(self):
        self.assertEqual(1, get_sol().mostBooked(3, [[1,20],[2,10],[3,5],[4,9],[6,8]]))
    # def test03(self):
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def testDummy1(self):
    # def testDummy2(self):
