import unittest
from typing import List


class Solution:
    def partition(self, s):
        def palindrome(s: str):
            if s == s[::-1]:
                return True
            return False

        def dfs(s, path, res):
            if not s:
                res.append(path[:])
                return
            for i in range(1, len(s) + 1):
                first, last = s[:i], s[i:]
                if palindrome(first):
                    path.append(s[:i])
                    dfs(last, path, res)
                    path.pop()

        res = []
        dfs(s, [], res)
        return res

    def partition2(self, s: str) -> List[List[str]]:
        res, n = [], len(s)

        def palindrome(s: str):
            if s == s[::-1]:
                return True
            return False

        def helper(s: str):
            res, n = [], len(s)
            if n == 1:
                res.append(s)
                return res
            if palindrome(s):
                res.append([s])
            for i in range(n - 1):
                first, second = s[:i + 1], s[i + 1:]
                if palindrome(first):
                    ans = helper(second)
                    for sub_ans in ans:
                        print('sub_ans type:', type(sub_ans))
                        res.append([first] + list(sub_ans))
            return res

        if n == 1:
            return [[s]]
        return helper(s)


class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.partition('ab')
        expected = [['a', 'b']]
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.partition(s="aab")
        expected = [["a", "a", "b"], ["aa", "b"]]
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.partition('bbaca')
        expected = [['b', 'b', 'aca'], ['b', 'b', 'a', 'c', 'a'], ['bb', 'aca'], ['bb', 'a', 'c', 'a']]
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.partition('a')
        expected = [['a']]
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        actual = sol.partition('aa')
        expected = [['a', 'a'], ['aa']]
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        actual = sol.partition('aabaa')
        expected = [[]]
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        actual = sol.partition(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        actual = sol.partition(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        actual = sol.partition(0)
        expected = 0
        self.assertEqual(expected, actual)
