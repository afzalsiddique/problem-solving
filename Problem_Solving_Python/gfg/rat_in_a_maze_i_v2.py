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

    def test_2(self):
        sol = Solution()
        mat = [[1, 1, 1, 1],
               [1, 1, 1, 1],
               [1, 1, 1, 1],
               [1, 1, 1, 1]]
        n = 4
        actual = sol.findPath(mat, n)
        expected = ['DDDRRR', 'DDDRRULURRDD', 'DDDRRULURURDDD', 'DDDRRULUURDRDD', 'DDDRRULUURRDDD', 'DDDRRURD', 'DDDRRUULURRDDD', 'DDDRRUURDD', 'DDDRRUUURDDD', 'DDDRURDR', 'DDDRURRD', 'DDDRURULURRDDD', 'DDDRURURDD', 'DDDRURUURDDD', 'DDDRUURDDR', 'DDDRUURDRD', 'DDDRUURRDD', 'DDDRUURRDLDR', 'DDDRUURURDDD', 'DDDRUURURDDLDR', 'DDDRUUURDDDR', 'DDDRUUURDDRD', 'DDDRUUURDRDD', 'DDDRUUURDRDLDR', 'DDDRUUURRDDD', 'DDDRUUURRDDLDR', 'DDDRUUURRDLDDR', 'DDDRUUURRDLDRD', 'DDRDRR', 'DDRDRURD', 'DDRDRUULURRDDD', 'DDRDRUURDD', 'DDRDRUUURDDD', 'DDRRDR', 'DDRRRD', 'DDRRULURRDDD', 'DDRRURDD', 'DDRRUURDDD', 'DDRURDDR', 'DDRURDRD', 'DDRURRDD', 'DDRURRDLDR', 'DDRURURDDD', 'DDRURURDDLDR', 'DDRUURDDDR', 'DDRUURDDRD', 'DDRUURDRDD', 'DDRUURDRDLDR', 'DDRUURRDDD', 'DDRUURRDDLDR', 'DDRUURRDLDDR', 'DDRUURRDLDRD', 'DRDDRR', 'DRDDRURD', 'DRDDRUURDD', 'DRDDRUUURDDD', 'DRDLDRRR', 'DRDLDRRURD', 'DRDLDRRUURDD', 'DRDLDRRUUURDDD', 'DRDRDR', 'DRDRRD', 'DRDRURDD', 'DRDRUURDDD', 'DRRDDR', 'DRRDLDRR', 'DRRDLLDRRR', 'DRRDRD', 'DRRRDD', 'DRRRDLDR', 'DRRRDLLDRR', 'DRRRDLLLDRRR', 'DRRURDDD', 'DRRURDDLDR', 'DRRURDDLLDRR', 'DRRURDDLLLDRRR', 'DRURDDDR', 'DRURDDLDRR', 'DRURDDLLDRRR', 'DRURDDRD', 'DRURDRDD', 'DRURDRDLDR', 'DRURDRDLLDRR', 'DRURDRDLLLDRRR', 'DRURRDDD', 'DRURRDDLDR', 'DRURRDDLLDRR', 'DRURRDDLLLDRRR', 'DRURRDLDDR', 'DRURRDLDLDRR', 'DRURRDLDLLDRRR', 'DRURRDLDRD', 'RDDDRR', 'RDDDRURD', 'RDDDRUURDD', 'RDDDRUUURDDD', 'RDDLDRRR', 'RDDLDRRURD', 'RDDLDRRUURDD', 'RDDLDRRUUURDDD', 'RDDRDR', 'RDDRRD', 'RDDRURDD', 'RDDRUURDDD', 'RDLDDRRR', 'RDLDDRRURD', 'RDLDDRRUURDD', 'RDLDDRRUUURDDD', 'RDLDDRURDR', 'RDLDDRURRD', 'RDLDDRURURDD', 'RDLDDRURUURDDD', 'RDLDRDRR', 'RDLDRDRURD', 'RDLDRDRUURDD', 'RDLDRDRUUURDDD', 'RDLDRRDR', 'RDLDRRRD', 'RDLDRRURDD', 'RDLDRRUURDDD', 'RDRDDR', 'RDRDLDRR', 'RDRDLLDRRR', 'RDRDRD', 'RDRRDD', 'RDRRDLDR', 'RDRRDLLDRR', 'RDRRDLLLDRRR', 'RDRURDDD', 'RDRURDDLDR', 'RDRURDDLLDRR', 'RDRURDDLLLDRRR', 'RRDDDR', 'RRDDLDRR', 'RRDDLLDRRR', 'RRDDLULDDRRR', 'RRDDRD', 'RRDLDDRR', 'RRDLDDRURD', 'RRDLDLDRRR', 'RRDLDLDRRURD', 'RRDLDRDR', 'RRDLDRRD', 'RRDLLDDRRR', 'RRDLLDDRRURD', 'RRDLLDDRURDR', 'RRDLLDDRURRD', 'RRDLLDRDRR', 'RRDLLDRDRURD', 'RRDLLDRRDR', 'RRDLLDRRRD', 'RRDRDD', 'RRDRDLDR', 'RRDRDLLDRR', 'RRDRDLLLDRRR', 'RRDRDLLULDDRRR', 'RRRDDD', 'RRRDDLDR', 'RRRDDLLDRR', 'RRRDDLLLDRRR', 'RRRDDLLULDDRRR', 'RRRDDLULDDRR', 'RRRDDLULDLDRRR', 'RRRDDLULLDDRRR', 'RRRDDLULLDRDRR', 'RRRDLDDR', 'RRRDLDLDRR', 'RRRDLDLLDRRR', 'RRRDLDLULDDRRR', 'RRRDLDRD', 'RRRDLLDDRR', 'RRRDLLDDRURD', 'RRRDLLDLDRRR', 'RRRDLLDLDRRURD', 'RRRDLLDRDR', 'RRRDLLDRRD', 'RRRDLLLDDRRR', 'RRRDLLLDDRRURD', 'RRRDLLLDDRURDR', 'RRRDLLLDDRURRD', 'RRRDLLLDRDRR', 'RRRDLLLDRDRURD', 'RRRDLLLDRRDR', 'RRRDLLLDRRRD']
        self.assertEqual(expected, actual)



