from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        problematic_letters = []
        valid = True
        counter = Counter(s)
        for letter in counter:
            if counter[letter] < k:
                problematic_letters.append(letter)
                valid = False
        if valid:
            return len(s)

        for letter in problematic_letters:
            s = s.replace(letter, ' ')
        strings_after_divide = s.split()

        ans = 0
        for string in strings_after_divide:
            ans = max(ans, self.longestSubstring(string, k))
        return ans
