from typing import List;


def get_sol(): return Solution()
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        res=0
        for s in sentences:
            res=max(res,len(s.split()))
        return res

