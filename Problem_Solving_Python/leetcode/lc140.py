# https://www.youtube.com/watch?v=WepWFGxiwRs
# accepted
import unittest
from typing import List

# don't understand why dp is slower? Ans: consider this case: ['aaaaaaaa'], ['a','aa','aaa','aaaa']
class Solution3: # AC. 32 ms
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        def helper(s,path):
            if len(s)==0:res.append(" ".join(path))
            n = len(s)
            for word in wordDict:
                w = len(word)
                if w>n:continue
                first,second = s[:w], s[w:]
                if first==word:
                    helper(second, path+[first])

        helper(s,[])
        return res

class Solution: # AC. 100 ms
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        def word_break(s):
            if s in dp: return dp[s]
            result = []
            for word in wordDict:
                n = len(word)
                if s[:n] == word:
                    if n == len(s):
                        result.append(word)
                    else:
                        ans = word_break(s[len(word):])
                        for sub_ans in ans:
                            result.append(word + " " + sub_ans)
            dp[s] = result
            return result

        return word_break(s)


class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        def word_break(s):
            if s in dp: return dp[s]
            n = len(s)
            result = []
            for i in range(1, n + 1):
                word = s[:i]
                if word in wordDict:
                    if n == len(word):
                        result.append(word)
                    else:
                        tmp = word_break(s[i:])
                        for item in tmp:
                            result.append(word + " " + item)
            dp[s] = result
            return result

        return word_break(s)
class MyTestCase(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        s = "catsanddog"
        wordDict = ["cat", "cats", "and", "sand", "dog"]
        actual = sorted(solution.wordBreak(s, wordDict))
        expected = sorted([
                      "cats and dog",
                      "cat sand dog"
                    ])
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        s = "pineapplepenapple"
        wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
        actual = sorted(solution.wordBreak(s, wordDict))
        expected = sorted([
                          "pine apple pen apple",
                          "pineapple pen apple",
                          "pine applepen apple"
                        ])
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        s = "applepineapple"
        wordDict = ["apple", "pine","pineapple"]
        actual = sorted(solution.wordBreak(s, wordDict))
        expected = sorted([
                            "apple pine apple",
                            "apple pineapple"
                        ])
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        s = "aaaaaaaaaa"
        wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa","aaaaaa"]
        actual = sorted(solution.wordBreak(s, wordDict))
        expected = [""]
        self.assertEqual(expected, actual)



    def test_5(self):
        solution = Solution()
        s = "mycatsanddog"
        wordDict = ["cat", "cats", "and", "sand", "dog","my"]
        actual = sorted(solution.wordBreak(s, wordDict))
        expected = sorted([
                      "cats and dog",
                      "cat sand dog"
                    ])
        self.assertEqual(expected, actual)