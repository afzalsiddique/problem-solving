import unittest; from typing import List;


def get_sol(): return Solution()
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        initial = 0
        cur=0
        tasks.sort(key=lambda x:(x[1]-x[0]),reverse=True)
        for act,pre in tasks:
            if cur<pre:
                required=pre-cur
                cur+=required
                initial+=required
            cur-=act
        return initial
class Solution2:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x:(x[1]-x[0]),reverse=True)
        current=0
        for actual,minn in tasks:
            if current<minn:
                current+=(minn-current)
            current-=actual
        return current+sum(t[0] for t in tasks)

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(8, get_sol().minimumEffort([[1,2],[2,4],[4,8]]))
    def test2(self):
        self.assertEqual(32, get_sol().minimumEffort( [[1,3],[2,4],[10,11],[10,12],[8,9]]))
    def test3(self):
        self.assertEqual(27, get_sol().minimumEffort([[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
