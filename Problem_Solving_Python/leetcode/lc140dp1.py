# https://www.youtube.com/watch?v=WepWFGxiwRs
# accepted
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        def word_break(s):
            if s in dp: return dp[s]
            result = []
            for w in wordDict:
                if s[:len(w)] == w:
                    if len(w) == len(s):
                        result.append(w)
                    else:
                        tmp = word_break(s[len(w):])
                        for t in tmp:
                            result.append(w + " " + t)
            dp[s] = result
            return result

        return word_break(s)
