class Solution:
    def isValid(self, s, k, di):
        for letter in s:
            if letter in di:
                di[letter] += 1
            else:
                di[letter] = 1
        for cnt in di.values():
            if cnt < k:
                return False
        return True

    def find_the_indices_of_the_problematic_letters(self, s, k, di):
        indices = []
        problematic_letters = []
        for letter in di:
            if di[letter] < k:
                problematic_letters.append(letter)
        for idx in range(len(s)):
            if s[idx] in problematic_letters:
                indices.append(idx)
        return indices

    def divide(self, s, indices):  # might return some empty strings
        strings_after_divide = []
        strings_after_divide.append(s[:indices[0]])  # first string after divide
        strings_after_divide.append(s[indices[-1] + 1:])  # last string after divide
        for i in range(len(indices) - 1):
            strings_after_divide.append(s[indices[i] + 1:indices[i + 1]])
        return strings_after_divide

    def longestSubstring(self, s: str, k: int) -> int:
        di = {}
        if self.isValid(s, k, di):
            return len(s)

        indices = self.find_the_indices_of_the_problematic_letters(s, k, di)
        strings_after_divide = self.divide(s, indices)
        ans = -1
        for string in strings_after_divide:
            ans = max(ans, self.longestSubstring(string, k))
        return ans
