def graphColoring(mat, m):
    def isCorrect(cur, color):
        for i in range(len(mat)):
            if (mat[cur][i] == 1 and colors[i] == color):
                return False
        return True

    def graphCol(m, cur):
        if cur == len(mat):
            return True

        for color in range(1, m + 1):
            if (isCorrect(cur, color)):
                colors[cur] = color
                if (graphCol(m, cur + 1)):
                    return True
                colors[cur] = 0
        return False

    v = len(mat)
    colors = [0] * v
    if graphCol(m, 0):
        # print(colors)
        return "YES"
    return "NO"
mat = [[0,1, 0],[1, 0, 1],[0, 1, 0]]
print(graphColoring(mat, 3))