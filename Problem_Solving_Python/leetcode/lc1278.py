import unittest;
import functools


def get_sol(): return Solution()
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        @functools.lru_cache(None)
        def cost(s:str):
            i,j=0,len(s)-1
            res=0
            while i<j:
                res+=s[i]!=s[j]
                i+=1; j-=1
            return res
        @functools.lru_cache(None)
        def dfs(s:str,k:int):
            if k==1:
                return cost(s)
            res=float('inf')
            for i in range(1,len(s)):
                first = s[:i]
                second=s[i:]
                res= min(res,cost(first)+dfs(second,k-1))
            return res

        return dfs(s,k)
class Solution2:
    def palindromePartition(self, s: str, k: int) -> int:
        @functools.lru_cache(None)
        def cost(s:str):
            cnt=0
            i,j=0,len(s)-1
            while i<j:
                if s[i]!=s[j]:
                    cnt+=1
                i+=1
                j-=1
            return cnt
        @functools.lru_cache(None)
        def recur(s:str,k:int):
            if k==0: return float('inf')
            if k>len(s): return float('inf')
            if k==1: return cost(s)
            # if s==s[::-1]: return 0 # wrong
            if len(s)==k: return 0
            res=float('inf')
            for i in range(len(s)):
                tmp=cost(s[:i+1])
                res=min(res,tmp+recur(s[i+1:],k-1))
            return res

        return recur(s,k)
class Solution3:
    def palindromePartition(self, s: str, k: int) -> int:
        @functools.lru_cache(None)
        def cost(i:int,j:int):
            cnt=0
            while i<j:
                if s[i]!=s[j]:
                    cnt+=1
                i+=1
                j-=1
            return cnt
        @functools.lru_cache(None)
        def recur(left: int, k: int):
            if k==0:
                return float('inf')
            if k>right-left+1:
                return float('inf')
            if k==1:
                return cost(left,right)
            if right-left+1==k:
                return 0
            res=float('inf')
            for mid in range(left,right):
                tmp=cost(left,mid)
                res=min(res, tmp + recur(mid + 1, k - 1))
            return res

        right=len(s)-1
        return recur(0, k)


class Solution4:
    # wrong
    def palindromePartition(self, s: str, k: int) -> int:
        @functools.lru_cache(None)
        def getCost(s:str):
            i,j=0,len(s)-1
            res=0
            while i<j:
                res+=s[i]!=s[j]
                i+=1
                j-=1
            return res
        def palindrome(s:str): return s==s[::-1]
        @functools.lru_cache(None)
        def dfs(s:str,k:int):
            if k==1:
                return getCost(s)
            res=float('inf')
            for i in range(1,len(s)):
                first = s[:i]
                second=s[i:]
                if palindrome(first):
                    res= min(res,dfs(second,k-1))
                elif palindrome(second):
                    res= min(res,dfs(first,k-1))
            return res

        return dfs(s,k)
class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(1,get_sol().palindromePartition(s = "abc", k = 2))
    def test02(self):
        self.assertEqual(0,get_sol().palindromePartition(s = "aabbc", k = 3))
    def test03(self):
        self.assertEqual(0,get_sol().palindromePartition(s = "leetcode", k = 8))
    def test04(self):
        self.assertEqual(4,get_sol().palindromePartition("oiwwhqjkb", 1))
    def test05(self):
        self.assertEqual(1,Solution().palindromePartition("yrici", 2))
    def test06(self):
        self.assertEqual(1,get_sol().palindromePartition("aea", 2))
    def test07(self):
        self.assertEqual(1,get_sol().palindromePartition("abab", 3))
    def test08(self):
        self.assertEqual(1,Solution().palindromePartition("ooyrincxiv", 5))
    def test09(self):
        self.assertEqual(1,Solution().palindromePartition("fhooxzyrincxiv", 10))
    def test10(self):
        self.assertEqual(20,get_sol().palindromePartition("fyhowoxzyrincxivwarjuwxrwealesxsimsepjdqsstfggjnjhilvrwwytbgsqbpnwjaojfnmiqiqnyzijfmvekgakefjaxryyml", 32))
