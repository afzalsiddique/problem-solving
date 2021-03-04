import unittest
from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        li = [0 for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if boxes[j] == '1':
                    li[i] += abs(j - i)
        return li

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.minOperations("110")
        expected = [1,1,3]
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.minOperations("001011")
        expected = [11,8,5,4,3,4]
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.minOperations(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.minOperations(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        actual = sol.minOperations(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        actual = sol.minOperations(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        actual = sol.minOperations(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        actual = sol.minOperations(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        actual = sol.minOperations(0)
        expected = 0
        self.assertEqual(expected, actual)