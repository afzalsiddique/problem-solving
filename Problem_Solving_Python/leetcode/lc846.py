import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/hand-of-straights/discuss/135598/C%2B%2BJavaPython-O(MlogM)-Complexity
    def isNStraightHand(self, hand, groupSize):
        n=len(hand)
        if n%groupSize: return False

        di = Counter(hand)
        for num in sorted(di):
            if di[num] > 0:
                for i in reversed(range(groupSize)): # don't like reversed iteration
                    di[num + i] -= di[num]
                    if di[num + i] < 0:
                        return False
        return True
class Solution2:
    # modified version of -> https://leetcode.com/problems/hand-of-straights/discuss/135598/C%2B%2BJavaPython-O(MlogM)-Complexity
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if n%groupSize: return False

        di = Counter(hand)
        for num in sorted(di.keys()): # simulating OrderedTree in Java
            while di[num] > 0:
                for i in range(groupSize): # a small change here from the first solution
                    if di[num+i] == 0: return False
                    di[num + i] -= 1
        return True

class Solution3:
    # modified version of -> https://leetcode.com/problems/hand-of-straights/discuss/135598/C%2B%2BJavaPython-O(MlogM)-Complexity
    # https://leetcode.com/problems/hand-of-straights/discuss/135598/C++JavaPython-O(MlogM)-Complexity/502962
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if n%groupSize: return False

        di = Counter(hand)
        hand = sorted(hand)
        for num in hand:
            if di[num]:
                for i in range(groupSize): # a small change here from the first solution
                    if not di[num + i]:
                        return False
                    else:
                        di[num + i] -= 1
        return True
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
