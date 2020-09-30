import unittest
from algorithms.knapsack01 import *

class MyTestCase(unittest.TestCase):
    def test_1(self):
        capacity = 7
        W = [3,1,3,4,2]
        V = [2,2,4,5,3]
        actual, items = knapsack(capacity, W, V)
        expected = 10
        self.assertEqual(expected, actual)
        expected = [5,4,2]
        self.assertEqual(expected, items)

if __name__ == '__main__':
    unittest.main()
