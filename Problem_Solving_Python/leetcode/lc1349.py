import unittest; from typing import List;


def get_sol(): return Solution()
class Solution:
    def maxStudents(self, mat: List[List[str]]) -> int:
        def count_bits(n):
            cnt = 0
            while n:
                cnt += 1
                n = n & (n - 1)
            return cnt

        m, n = len(mat), len(mat[0])
        totalComb=1<<n
        rows = []
        rows.append('dummy')

        for i in range(m):
            seats = 0
            for j in range(n):
                seats = (seats << 1) + (mat[i][j] == '.')
            rows.append(seats)

        # dp[i][j] represents max no of students can seated from 0 upto ith row with 'j' student configuration in the ith row
        dp = [[-1] * totalComb for _ in range(m + 1)]
        dp[0][0] = 0 #
        for i in range(1, m + 1):
            seats = rows[i]
            for curStudents in range(totalComb):
                if not curStudents & seats == curStudents: continue # if students are not seated in the good seats
                if curStudents & (curStudents>>1): continue # no students can seat another students left or right side
                for prevStudents in range(totalComb):
                    if curStudents & (prevStudents>>1): continue # upper-right in the previous row
                    if curStudents & (prevStudents<<1): continue # upper-left in the previous row
                    if dp[i-1][prevStudents]==-1: continue # invalid dp state
                    dp[i][curStudents] = max(dp[i][curStudents], dp[i-1][prevStudents] + count_bits(curStudents))

        return max(dp[-1])
class Solution2:
    # tle
    def maxStudents(self, mat: List[List[str]]) -> int:
        def noOfStudents():
            return sum(mat[i][j]=='s' for i in range(m) for j in range(n))
        def valid(idx): # if it is possible to place a student at this seat
            i,j=li[idx]
            if mat[i][j]=='#': return False # seat is broken. not possible to place a student
            for di,dj in [(-1,-1),(0,-1),(-1,1),(0,1)]:
                x,y=i+di,j+dj
                if not 0<=x<m or not 0<=y<n: continue
                if mat[x][y]=='s':
                    return False
            return True
        def dfs(idx:int): # idx th non-broken empty seat
            if idx==len(li):
                return noOfStudents()
            res=float('-inf')
            res=max(res,dfs(idx+1)) # keep this seat empty
            if valid(idx): # if possible place a student at this seat
                i,j=li[idx]
                mat[i][j]='s' # place a student
                res=max(res,dfs(idx+1))
                mat[i][j]='.' # remove a student
            return res

        m,n= len(mat), len(mat[0])
        li=[[i,j] for i in range(m) for j in range(n) if mat[i][j] == '.']
        return dfs(0)

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(4, Solution().maxStudents([["#",".","#","#",".","#"],
                                                    [".","#","#","#","#","."],
                                                    ["#",".","#","#",".","#"]]))
    def test02(self):
        self.assertEqual(3, Solution().maxStudents([[".","#"],
                                                    ["#","#"],
                                                    ["#","."],
                                                    ["#","#"],
                                                    [".","#"]]))
    def test03(self):
        self.assertEqual(10, Solution().maxStudents([["#",".",".",".","#"],
                                                     [".","#",".","#","."],
                                                     [".",".","#",".","."],
                                                     [".","#",".","#","."],
                                                     ["#",".",".",".","#"]]))
    def test04(self):
        self.assertEqual(31, Solution().maxStudents([[".",".",".",".","#",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".","#","."],[".",".",".",".",".",".",".","."],[".",".","#",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","#",".",".","#","."]]))
