# https://www.youtube.com/watch?v=CxrnOTUlNJE
import math
import unittest
from typing import List




class Solution:
    def reverseWords(self, s: str) -> str:
        s = s+" " # if there is no space at the end, the last word won't be added. That's why we add an extra space
        words = []
        word_so_far = []
        for ch in s:
            if ch != ' ':
                word_so_far.append(ch)
            else:
                # Avoid adding empty words when encountered multiple spaces.
                if word_so_far:
                    words.append(''.join(word_so_far))
                    word_so_far = []  # Reset
        result = ""
        for word in words:
            result = word + " " + result
        result = result[:-1]
        return result

class Solution2:
    def reverseWords(self, s: str) -> str:
        for i in range(len(s)):
            if s[i]!=' ':
                s=s[i:]
                break
        for i in reversed(range(len(s))):
            if s[i]!=' ':
                s=s[:i+1]
                break
        dummy_space = ' '
        s=s[::-1] + dummy_space
        n=len(s)
        res=[]
        left,right=0,0
        while right<=n-1:
            if s[right]==' ':
                temp=[]
                while left<right:
                    temp.append(s[left])
                    left+=1
                res.append(temp[::-1])
                while right<=n-1 and s[right]==' ':
                    right+=1
                left=right
            right+=1
        new_res = []
        for x in res:
            new_res.append(''.join(x))
        return ' '.join(new_res)
class Case(unittest.TestCase):
    def test_1(self):
        s = "  bob  loves  alice  "
        a = Solution().reverseWords(s)
        e = "alice loves bob"
        self.assertEqual(e, a)
    def test_2(self):
        s = "the sky is blue"
        a = Solution().reverseWords(s)
        e = "blue is sky the"
        self.assertEqual(e, a)

    def test_3(self):
        sol = Solution()
        actual = sol.reverseWords("Bob  Loves")
        expected = "Loves Bob"
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.reverseWords("Bob  Loves")
        expected = "Loves Bob"
        self.assertEqual(expected, actual)
