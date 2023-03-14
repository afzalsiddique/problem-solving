def get_sol(): return Solution()
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num==0: return True
        s=str(num)
        if s[0]=='0' or s[-1]=='0':
            return False
        return True

