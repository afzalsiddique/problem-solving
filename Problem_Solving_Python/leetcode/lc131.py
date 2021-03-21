import unittest
from typing import List


class Solution:

    ######## THOUGH MEMOIZED VERSION BUT THIS IS NOT BETTER IN TIME COMPLEXITY ##############
    def partition(self, s: str) -> List[List[str]]:
        dp = {}

        def palindrome(s:str):
            n=len(s)
            if n==0 or n==1:return True
            if n==2: return s[0]==s[1]
            if s[0]==s[-1]:
                return palindrome(s[1:-1])
            return False

        def helper(s:str):
            if len(s)==1:return [[s]]
            if not s: return [[]]
            if s in dp:return dp[s]

            all_results = []
            for i in range(1,len(s)+1):
                first,second = s[:i], s[i:]
                if palindrome(first):
                    ans = helper(second)
                    result = []
                    for sub_ans in ans:
                        result.append([first]+sub_ans)
                    all_results+=result
            dp[s] = all_results
            return dp[s]


        return helper(s)

    def partition2(self, s):
        def palindrome(s: str):
            if s == s[::-1]:
                return True
            return False

        def dfs(s,path):
            if not s:
                res.append(path)
                return
            for i in range(1, len(s) + 1):
                first, last = s[:i], s[i:]
                if palindrome(first):
                    dfs(last, path + [first])

        res = []
        dfs(s,[])
        return res

    def partition3(self, s: str) -> List[List[str]]:
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
        self.assertEqual(sorted(expected),sorted( actual))


    def test_3(self):
        sol = Solution()
        actual = sol.partition('bbaca')
        expected = [['b', 'b', 'aca'], ['b', 'b', 'a', 'c', 'a'], ['bb', 'aca'], ['bb', 'a', 'c', 'a']]
        self.assertEqual(sorted(expected),sorted( actual))

    def test_4(self):
        sol = Solution()
        actual = sol.partition('a')
        expected = [['a']]
        self.assertEqual(sorted(expected),sorted( actual))

    def test_5(self):
        sol = Solution()
        actual = sol.partition('aa')
        expected = [['a', 'a'], ['aa']]
        self.assertEqual(sorted(expected),sorted( actual))


    def test_6(self):
        sol = Solution()
        actual = sol.partition('aabaa')
        expected = [['a', 'a', 'b', 'a', 'a'],
 ['a', 'a', 'b', 'aa'],
 ['a', 'aba', 'a'],
 ['aa', 'b', 'a', 'a'],
 ['aa', 'b', 'aa'],
 ['aabaa']]
        self.assertEqual(sorted(expected),sorted( actual))
