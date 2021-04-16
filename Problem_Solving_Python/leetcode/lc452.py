# https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/discuss/93735/A-Concise-Template-for-%22Overlapping-Interval-Problem%22
import unittest
from typing import List
## similar ###
# 56 Merge Intervals
# 435 Non-overlapping Intervals
# 252 Meeting Rooms
# 253 Meeting Rooms II

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # if len(points)==0:return 0
        points.sort(key=lambda x:x[1])
        shoot, cnt = float('-inf'),0
        shoots = []
        for start,end in points:
            if shoot<start:
                cnt+=1
                shoot=end
                shoots.append(shoot)
        print(shoots)
        return cnt

    def findMinArrowShots2(self, points):
        points.sort(reverse=True)
        shoot,cnt = float('inf'), 0
        shoots = []
        for start, end in points:
            if shoot > end:
                cnt += 1
                shoot = start
                shoots.append(shoot)
        print(shoots)
        return cnt

    def findMinArrowShots3(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        arrow ,shoot= 0,-1
        for start, end in points:
            if start<=shoot<=end: continue
            shoot = end
            arrow+=1
        return arrow



class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        points = [[10, 16], [2, 8], [1, 6], [7, 12]]
        actual = sol.findMinArrowShots(points)
        expected = 2
        self.assertEqual(expected, actual)
        actual = sol.findMinArrowShots2(points)
        expected = 2
        self.assertEqual(expected,actual)

    def test_2(self):
        sol = Solution()
        points = [[1,2],[3,4],[5,6],[7,8]]
        actual = sol.findMinArrowShots(points)
        expected = 4
        self.assertEqual(expected, actual)
        actual = sol.findMinArrowShots2(points)
        expected = 4
        self.assertEqual(expected,actual)

    def test_3(self):
        sol = Solution()
        points = [[1,2],[2,3],[3,4],[4,5]]
        actual = sol.findMinArrowShots(points)
        expected = 2
        self.assertEqual(expected, actual)
        actual = sol.findMinArrowShots2(points)
        expected = 2
        self.assertEqual(expected,actual)

    def test_4(self):
        sol = Solution()
        actual = sol.findMinArrowShots([[1,2]])
        expected = 1
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        actual = sol.findMinArrowShots([[2,3],[2,3]])
        expected = 1
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        actual = sol.findMinArrowShots([])
        expected = 0
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        actual = sol.findMinArrowShots([[-2147483648,2147483647]])
        expected = 1
        self.assertEqual(expected, actual)
