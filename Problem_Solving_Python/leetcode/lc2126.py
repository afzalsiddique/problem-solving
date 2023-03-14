import unittest; from typing import List;


def get_sol(): return Solution()
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for a in asteroids:
            if a>mass:
                return False
            mass+=a
        return True


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(True, get_sol().asteroidsDestroyed(mass = 10, asteroids = [3,9,19,5,21]))
    def test2(self):
        self.assertEqual(False, get_sol().asteroidsDestroyed(mass = 5, asteroids = [4,9,23,4]))
    # def test3(self):
        # self.assertEqual(1, get_sol().asteroidsDestroyed())
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
