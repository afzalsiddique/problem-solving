from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0 or n == 1:
            return n
        di = defaultdict(int)
        left, right = 0, 0
        ans = 0
        di[s[left]] += 1
        while right != n - 1:
            if di[s[right + 1]] == 0:
                di[s[right + 1]] += 1
                right += 1
            elif left == right:
                di[s[left]] -= 1
                di[s[right + 1]] += 1
                left += 1
                right += 1
            elif di[s[right + 1]] == 1:
                di[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
