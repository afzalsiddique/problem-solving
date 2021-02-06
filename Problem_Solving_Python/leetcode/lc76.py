# https://leetcode.com/problems/minimum-window-substring/discuss/26810/Java-solution.-using-two-pointers-+-HashMap/260540
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == 0 or len(t)==0 or len(s) < len(t): return ""
        n = len(s)
        di = defaultdict(int)
        flag = False
        missing = len(t)
        for letter in t:
            di[letter]+=1
        i,j,min_left,min_right = 0,0,0,0
        minn = float('inf')
        while j < n: # ith & jth char are included in the window
            c_right = s[j]
            if c_right in di:
                di[c_right]-=1 # negative value in the dict means extra characters or useless characters are inside window. s='ABBBC', t = 'ABC'. Here  at some point di['B']=-2.
                if di[c_right] >= 0: # found a useful char.
                    missing-=1
            # if found a susbtring
            while missing == 0 and i <= j:
                flag = True # flag is required because ith and jth char are included in the window
                cur_len = j - i + 1
                if cur_len < minn:
                    min_left, min_right = i,j
                    minn = cur_len
                # move left_pointer to the right
                c_left = s[i]
                if c_left in di:
                    di[c_left] += 1
                    if di[c_left] >= 1: # a useful char will be removed
                        missing+=1
                i+=1
            j+=1
        return s[min_left:min_right+1] if flag else ""