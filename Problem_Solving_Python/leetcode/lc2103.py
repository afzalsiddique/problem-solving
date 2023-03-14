def get_sol(): return Solution()
class Solution:
    def countPoints(self, rings: str) -> int:
        n=len(rings)
        i=0
        arr=[set() for _ in range(10)]
        while i<n:
            arr[int(rings[i+1])].add(rings[i])
            i+=2
        return sum([True for x in arr if len(x)==3])
