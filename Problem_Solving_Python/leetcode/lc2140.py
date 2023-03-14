import unittest; from typing import List; import functools


def get_sol(): return Solution()
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def dfs(i):
            if i>=n:
                return 0
            points,noOfSkip=questions[i]
            skip=dfs(i+1)
            take=points+dfs(i+1+noOfSkip)
            return max(skip,take)

        n=len(questions)
        return dfs(0)

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(5,get_sol().mostPoints([[3,2],[4,3],[4,4],[2,5]]))
    def test2(self):
        self.assertEqual(7,get_sol().mostPoints([[1,1],[2,2],[3,3],[4,4],[5,5]]))
    # def test3(self):
    # def test4(self):
    # def test5(self):
