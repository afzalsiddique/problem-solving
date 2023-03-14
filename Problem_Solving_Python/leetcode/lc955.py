import unittest; from typing import List;


def get_sol(): return Solution()
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        m, n = len(A), len(A[0])
        ans, in_order = 0, [False] * (m-1)
        for j in range(n):
            tmp_in_order = in_order[:]
            for i in range(m-1):
                if in_order[i]:
                    continue
                # previous step, rows are not in order; and current step rows are not in order, remove this column
                if A[i][j] > A[i+1][j]:
                    ans += 1; break
                # previous step, rows are in order now
                elif A[i][j] < A[i+1][j]:
                    tmp_in_order[i] = True
            # if column wasn't removed, update the row order information
            else:
                in_order = tmp_in_order
            # not necessary, but speed things up
            if all(in_order): return ans
        return ans

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(1, get_sol().minDeletionSize(["ca","bb","ac"]))
    def test02(self):
        self.assertEqual(0, get_sol().minDeletionSize(["xc","yb","za"]))
    def test03(self):
        self.assertEqual(3, get_sol().minDeletionSize(["zyx","wvu","tsr"]))
    def test04(self):
        self.assertEqual(6, get_sol().minDeletionSize(["zyxwvu","abcdef","adfksha"]))
    def test05(self):
        self.assertEqual(1, get_sol().minDeletionSize(["xga","xfb","yfa"]))
    def test06(self):
        self.assertEqual(2, get_sol().minDeletionSize(["vdy","vei","zvc","zld"]))
    # def test07(self):
