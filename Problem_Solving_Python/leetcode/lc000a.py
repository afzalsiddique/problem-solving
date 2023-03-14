import unittest; from typing import List;


def get_sol(): return Solution()
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n=len(matrix)
        for i in range(n):
            sett=set()
            for j in range(n):
                if not 1<=matrix[i][j]<=n:
                    return False
                if matrix[i][j] in sett:
                    return False
                sett.add(matrix[i][j])

        for j in range(n):
            sett=set()
            for i in range(n):
                if not 1<=matrix[i][j]<=n:
                    return False
                if matrix[i][j] in sett:
                    return False
                sett.add(matrix[i][j])
        return True


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(3, get_sol().maximumInvitations([2,2,1,2]))
    def test2(self):
        self.assertEqual(3, get_sol().maximumInvitations([1,2,0]))
    def test3(self):
        self.assertEqual(4, get_sol().maximumInvitations([3,0,1,4,1]))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
