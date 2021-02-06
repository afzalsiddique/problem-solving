# https://www.youtube.com/watch?v=1xfx6M_GqFk
class Solution:
    def numSquares(self, n: int) -> int:
        di = {}
        def helper(n):
            if n<=3:
                return n
            if n in di:
                return di[n]
            minn = float('inf')
            i = 1
            while i*i<=n:
                temp = helper(n-i*i)
                minn = min(minn, temp)
                i+=1
            di[n] = minn+1
            return di[n]
        return helper(n)
