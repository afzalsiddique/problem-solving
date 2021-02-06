import unittest
from bisect import bisect_right
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n=len(intervals)
        times = [x[0] for x in intervals]
        di={}
        for i,time in enumerate(times):
            di[time] = i

        times.sort()

        ret=[]
        for interval in intervals:
            target=interval[1]
            idx=bisect_right(times,target)
            if idx!=0 and times[idx-1]==target: # next start is equal to this end
                ret.append(di[times[idx-1]])
            elif idx<n: # next start is greater than this end
                ret.append(di[times[idx]])
            else:
                ret.append(-1)
        return ret



class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        expected = [2,-1,-1,2,3]
        actual = sol.findRightInterval([[1,3],[1,4],[3,4],[2,3],[1,2]])
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        expected = [-1]
        actual = sol.findRightInterval([[1,2]])
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        expected = [-1,0,1]
        actual = sol.findRightInterval([[3,4],[2,3],[1,2]])
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        expected =[-1,2,-1]
        actual = sol.findRightInterval([[1,4],[2,3],[3,4]])
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        expected = [-1,0,1]
        actual = sol.findRightInterval([[4,5],[2,3],[1,2]])
        self.assertEqual(expected, actual)

