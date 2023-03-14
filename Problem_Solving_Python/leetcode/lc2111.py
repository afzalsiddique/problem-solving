import unittest; from typing import List;


def get_sol(): return Solution()
class Solution:
    # wrong
    def kIncreasing(self, arr: List[int], k: int) -> int:
        n=len(arr)
        res=0
        for i in range(k,n):
            if arr[i]<arr[i-k]:
                arr[i-k]=arr[i]
                res+=1
        return res


class Tester(unittest.TestCase):
    def test_1(self):
        self.assertEqual(4,get_sol().kIncreasing(arr = [5,4,3,2,1], k = 1))
    def test_2(self):
        self.assertEqual(0,get_sol().kIncreasing(arr = [4,1,5,2,6,2], k = 2))
    def test_3(self):
        self.assertEqual(2,get_sol().kIncreasing(arr = [4,1,5,2,6,2], k = 3))
    def test_4(self):
        self.assertEqual(0,get_sol().kIncreasing(arr = [2,2,2,2,2], k = 3))
    def test_5(self):
        self.assertEqual(0,get_sol().kIncreasing(arr = [1,2,3,4,5,6], k = 3))
    def test_6(self):
        self.assertEqual(1,get_sol().kIncreasing(arr = [7,6,5,4,6,5,4], k = 3))
    def test_7(self):
        self.assertEqual(12,get_sol().kIncreasing([12,6,12,6,14,2,13,17,3,8,11,7,4,11,18,8,8,3], 1))
    # def test_8(self):
    # def test_9(self):
