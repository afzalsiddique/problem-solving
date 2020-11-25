class Solution:
    def isValid(self, s, k, problematic_letter):
        di = {}
        for letter in s:
            if letter in di:
                di[letter] += 1
            else:
                di[letter] = 1
        ans = True
        for letter in di:
            if di[letter] < k:
                problematic_letter.append(letter)
                ans = False
        return ans

    def longestSubstring(self, s: str, k: int) -> int:
        problematic_letters = []
        if self.isValid(s, k, problematic_letters):
            return len(s)

        for letter in problematic_letters:
            s = s.replace(letter, ' ')
        strings_after_divide = s.split()

        ans = 0
        for string in strings_after_divide:
            ans = max(ans, self.longestSubstring(string, k))
        return ans
