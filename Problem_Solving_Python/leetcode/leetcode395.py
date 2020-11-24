from collections import Counter


class Solution:
    def isValid(self, s, k): # before calling this method check if the string is empty
        counter = Counter(s)
        for letter in counter:
            if counter[letter] < k:
                return False
        return True

    def tell_me_where_to_divide(self, s, k):
        indices = []
        problematic_letters = []
        counter = Counter(s)
        for letter in counter:
            if counter[letter] < k:
                problematic_letters.append(letter)
        for idx in range(len(s)):
            if s[idx] in problematic_letters:
                indices.append(idx)
        return indices

    def divide_and_return(self, s, indices): # might return some empty strings
        strings_after_divide = [s[:indices[0]], s[indices[-1] + 1:]] # first and last string
        for i in range(len(indices)-1):
            strings_after_divide.append(s[indices[i] + 1:indices[i + 1]])
        return strings_after_divide

    def longestSubstring(self, s: str, k: int) -> int:
        if len(s)==0:
            return 0
        if self.isValid(s, k):
            return len(s)

        indices = self.tell_me_where_to_divide(s, k)
        strings_after_divide = self.divide_and_return(s, indices)
        ans = -1
        for string in strings_after_divide:
            ans = max(ans, self.longestSubstring(string, k))
        return ans


