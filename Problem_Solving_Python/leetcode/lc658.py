# https://www.youtube.com/watch?v=J8yLD-x7fBI
import unittest
from bisect import bisect_left
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n=len(arr)
        diff=[abs(x-item) for item in arr]
        summ=minn=sum(diff[:k])

        i,start=0,0
        while i+k!=n:
            summ-=diff[i]
            summ+=diff[i+k]
            i+=1

            if summ<minn:
                minn=summ
                start=i
        return arr[start:start+k]


class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        expected = [1,2,3,4]
        actual = sol.findClosestElements( arr = [1,2,3,4,5], k = 4, x = 3)
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        expected = [380,390]
        actual = sol.findClosestElements( arr = [380,390,420,430,440], k = 2, x = 399)
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        expected = [1,2,3,4]
        actual = sol.findClosestElements(arr = [1,2,3,4,5], k = 4, x = -1)
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        expected = [3,4,6,7]
        actual = sol.findClosestElements([0,2,2,3,4,6,7,8,9,9], 4, 5)
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        expected = [8,10]
        actual = sol.findClosestElements([3,5,8,10],2,15)
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        expected = [1]
        actual = sol.findClosestElements([1,3],1,2)
        self.assertEqual(expected, actual)