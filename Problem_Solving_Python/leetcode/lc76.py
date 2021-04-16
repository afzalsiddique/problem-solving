# https://leetcode.com/problems/minimum-window-substring/discuss/26810/Java-solution.-using-two-pointers-+-HashMap/260540
import unittest
from collections import defaultdict, Counter
# similar to 438
# https://leetcode.com/problems/minimum-window-substring/discuss/226911/Python-two-pointer-sliding-window-with-explanation
# https://www.youtube.com/watch?v=U1q16AFcjKs&t=90s
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required = Counter(t)
        i, j, found = 0, len(s)-1, 0
        min_win = ""
        for j in range(len(s)):
            right_letter = s[j]
            if required[right_letter]>0:found += 1
            required[right_letter] -=1
            while found==len(t):
                left_letter = s[i]
                #print(i, j, required)
                if not min_win or j-i+1<len(min_win):
                    min_win = s[i:j+1]
                required[left_letter]+=1
                if required[left_letter]>0:found -=1
                i+=1
        return min_win

class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:return ""
        di,missing = defaultdict(int), len(t)
        ans = float("inf"), None, None
        l,r = 0,0
        for letter in t:
            di[letter]+=1
        while r < len(s):
            c_right = s[r]
            if c_right in di:
                di[c_right]-=1 # negative value in the dict means extra characters or useless characters are inside window. s='ABBBC', t = 'ABC'. Here  at some point di['B']=-2.
                if di[c_right] >= 0: # found a useful char.
                    missing-=1
            # if found a susbtring
            while not missing and l <= r:
                cur_len = r - l + 1
                if cur_len < ans[0]:
                    ans = (r-l+1,l,r)
                # move left_pointer to the right
                c_left = s[l]
                if c_left in di:
                    di[c_left] += 1
                    if di[c_left] >= 1: # a useful char will be removed
                        missing+=1
                l+=1
            r+=1
        return "" if ans[0]==float('inf') else s[ans[1]:ans[2]+1]

class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual('BANC', Solution().minWindow(s = "ADOBECODEBANC", t = "ABC"))
    def test2(self):
        self.assertEqual('a', Solution().minWindow(s = "a", t = "a"))
    def test3(self):
        self.assertEqual('', Solution().minWindow(s = "a", t = "b"))
