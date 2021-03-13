class Solution:
    def romanToInt(self, s: str) -> int:
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