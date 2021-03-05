import unittest


class Solution:
    def findPath(self, mat, n):
        def dfs(row, col):
            if row==col==n-1 and mat[row][col]==1:
                res.append(''.join(path[:]))
                return
            mat[row][col]=0
            if row+1<n and mat[row+1][col]==1:
                path.append('D')
                dfs(row+1, col)
                path.pop(-1)
            if col-1>=0 and mat[row][col-1]==1:
                path.append('L')
                dfs(row, col-1)
                path.pop(-1)
            if col+1<n and mat[row][col+1]==1:
                path.append('R')
                dfs(row,col+1)
                path.pop(-1)
            if row-1>=0 and mat[row-1][col]==1:
                path.append('U')
                dfs(row-1,col)
                path.pop(-1)
            mat[row][col]=1


        res,path = [],[]
        if mat[0][0]!=1:return []
        dfs(0,0)
        return res

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        mat = [[1, 0, 0, 0],
                 [1, 1, 0, 1],
                 [1, 1, 0, 0],
                 [0, 1, 1, 1]]
        n = 4
        actual = sol.findPath(mat, n)
        expected = ['DDRDRR', 'DRDDRR']
        self.assertEqual(expected, actual)



# print(findPath(mat,n))


mat =   [[1, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 1, 1]]
n = 4
print(findPath(mat,n))