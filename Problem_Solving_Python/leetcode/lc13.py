from collections import defaultdict


class Solution:
    def romanToInt(self, s: str) -> int:
        value = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        di = defaultdict(str)
        di['I'] = 'VX'
        di['X'] = 'LC'
        di['C'] = 'DM'
        di['dummy'] = ''
        last = 'dummy'
        ans = 0
        for c in s:
            ans += value[c]
            if c in di[last]:
                ans -= 2*value[last]
            last = c
        return ans
    def romanToInt2(self, s: str) -> int:
        val = {'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'Z':0}
        di = {'I':'VX','X':'LC','C':'DM','V':'','L':'','D':'','M':'','Unknown':'IVXLCDM'}
        last = 'Unknown'
        ans = 0
        for ch in s:
            if ch in di[last]:
                ans += val[ch] - 2 * val[last]
            else:
                ans += val[ch]
            last = ch
        return ans