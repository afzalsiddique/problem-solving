def get_sol(): return Solution()
class Solution:
    def checkString(self, s: str) -> bool:
        bFound=False
        for x in s:
            if x=='b':
                bFound=True
            if bFound and x=='a':
                return False
        return True



