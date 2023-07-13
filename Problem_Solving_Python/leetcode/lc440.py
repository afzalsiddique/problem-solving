import unittest;


def get_sol(): return Solution()
class Solution:
    # lexicographically 1,10,100,1000.
    # If within range we can get the next number by multiplying with 10
    # If outside range then add 1. If 100 outside range then add 1. 10+1=11. 11 comes after 10.
    # https://www.youtube.com/watch?v=s3y1l3KV8bM
    def findKthNumber(self, n: int, k: int) -> int:
        # count how many numbers are there within the range starting at cur
        def count(cur): # count no of nodes in the subtree rooted at cur
            cnt=0
            level=0
            while cur<=n:
                cnt+=min(n-cur+1,10**level)
                cur*=10
                level+=1
            return cnt

        k-=1 # 0 indexed
        cur=1
        while k>0:
            cnt= count(cur)
            if k>=cnt:
                cur+=1
                k-=cnt
            else:
                cur*=10
                k-=1
        return cur


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(10, get_sol().findKthNumber(n = 13, k = 2))
    def test2(self):
        self.assertEqual(1, get_sol().findKthNumber(n = 1, k = 1))
    def test3(self):
        self.assertEqual(23, get_sol().findKthNumber(n=123,k=40))
    def test4(self):
        self.assertEqual(8, get_sol().findKthNumber(n=23,k=22))
    # def test5(self):
    # def test6(self):
    # def test7(self):

