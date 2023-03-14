import unittest; from typing import List;


def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/discuss/754623/Detailed-Explanation
    def minNumberOperations(self, target: List[int]) -> int:
        operationWeCanReuse=target[0]
        res=target[0]
        for i in range(1,len(target)):
            if target[i]>operationWeCanReuse:
                res+=target[i]-operationWeCanReuse
                operationWeCanReuse=target[i]
            else:
                operationWeCanReuse=target[i]
        return res
# class Solution2:
    # segment tree
    # def minNumberOperations(self, target: List[int]) -> int:

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, get_sol().minNumberOperations([1,2,3,2,1]))
    def test2(self):
        self.assertEqual(4, get_sol().minNumberOperations([3,1,1,2]))
    def test3(self):
        self.assertEqual(7, get_sol().minNumberOperations([3,1,5,4,2]))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
