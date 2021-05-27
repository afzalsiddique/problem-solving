import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
# same as 1296

class Solution:
    # https://leetcode.com/problems/hand-of-straights/discuss/135598/C%2B%2BJavaPython-O(MlogM)-Complexity
    def isNStraightHand(self, hand, groupSize):
        remaining = Counter(hand)

        for num in sorted(remaining): # simulating OrderedTree in Java
            if not remaining[num]: continue
            while remaining[num]:
                for i in range(groupSize):
                    if not remaining[num+i]:
                        return False
                    remaining[num+i]-=1
        return True
class Solution2:
    # modified version of -> https://leetcode.com/problems/hand-of-straights/discuss/135598/C%2B%2BJavaPython-O(MlogM)-Complexity
    # https://leetcode.com/problems/hand-of-straights/discuss/135598/C++JavaPython-O(MlogM)-Complexity/502962
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        remaining = Counter(hand)

        hand.sort()
        for num in hand:
            if not remaining[num]: continue
            for i in range(groupSize):
                if not remaining[num + i]: return False
                remaining[num + i] -= 1
        return True
class Solution3:
    # https://leetcode.com/problems/hand-of-straights/discuss/135598/C%2B%2BJavaPython-O(MlogM)-Complexity
    def isNStraightHand(self, hand, groupSize):
        remaining = Counter(hand)
        for num in sorted(remaining): # simulating OrderedTree in Java
            if remaining[num] > 0:
                for i in reversed(range(groupSize)):  # it's reversed because if you do it in the normal order, c[i] will become 0 first, then the rest will be all wrong.
                    remaining[num + i] -= remaining[num]
                    if remaining[num + i] < 0:
                        return False
        return True
# class Solution2:
#     bad solution
#     # modified version of -> https://leetcode.com/problems/hand-of-straights/discuss/135598/C%2B%2BJavaPython-O(MlogM)-Complexity
#     def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
#         n=len(hand)
#         if n%groupSize: return False
#
#         di = Counter(hand)
#         for num in sorted(di.keys()): # simulating OrderedTree in Java
#             while di[num] > 0:
#                 for i in range(groupSize): # a small change here from the first solution
#                     if di[num+i] == 0: return False
#                     di[num + i] -= 1
#         return True
class Solution4:
    # slow
    def add(self,num,groups,groupSize)->bool:
        for group in groups:
            if len(group)==0:
                group.append(num)
                return True
            else:
                if len(group)<groupSize:
                    if group[-1]==num-1:
                        group.append(num)
                        return True
        return False
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if n%groupSize: return False
        groups_no=n//groupSize
        groups=[[] for _ in range(groups_no)]
        pq = hand
        heapify(pq)
        while pq:
            num = heappop(pq)
            if self.add(num,groups,groupSize):
                pass
            else:
                return False
        return True

class MyTestCase(unittest.TestCase):
    def test01(self):
        hand = [1,2,3,6,2,3,4,7,8]
        groupSize = 3
        Output= True
        self.assertEqual(Output, get_sol().isNStraightHand(hand, groupSize))
    def test02(self):
        hand = [1,2,3,4,5]
        groupSize = 4
        Output= False
        self.assertEqual(Output, get_sol().isNStraightHand(hand, groupSize))
    def test03(self):
        hand = [8,10,12]
        groupSize = 3
        Output= False
        self.assertEqual(Output, get_sol().isNStraightHand(hand, groupSize))
    def test04(self):
        hand = [1,1,2,2,3,3]
        groupSize = 3
        Output= True
        self.assertEqual(Output, get_sol().isNStraightHand(hand, groupSize))
