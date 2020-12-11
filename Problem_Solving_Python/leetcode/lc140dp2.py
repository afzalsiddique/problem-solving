# https://www.youtube.com/watch?v=WepWFGxiwRs
# accepted
from typing import List


class Solution:
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
