import unittest
from typing import List


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        li=[]
        if n1<n2:
            for i in range(n1):
                li.append(word1[i])
                li.append(word2[i])
            for i in range(n1,n2):
                li.append(word2[i])
        else:
            for i in range(n2):
                li.append(word1[i])
                li.append(word2[i])
            for i in range(n2,n1):
                li.append(word1[i])
        return "".join(li)

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.mergeAlternately(word1 = "abc", word2 = "pqr")
        expected = "apbqcr"
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.mergeAlternately(word1 = "ab", word2 = "pqrs")
        expected = "apbqrs"
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.mergeAlternately(word1 = "abcd", word2 = "pq")
        expected = "apbqcd"
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.mergeAlternately("a","b")
        expected = "ab"
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        actual = sol.mergeAlternately("qwer","asdf")
        expected = "qawsedrf"
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        actual = sol.mergeAlternately("q","asdfghj")
        expected = "qasdfghj"
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        actual = sol.mergeAlternately("asdfghj","q")
        expected = "aqsdfghj"
        self.assertEqual(expected, actual)

