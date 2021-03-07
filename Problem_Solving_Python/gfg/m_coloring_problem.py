def graphColoring(mat,m):

    def valid(vertex, color):
        for i in range(len(mat)):
            if mat[vertex][i]==1 and colors[i]==color:
                return False
        return True

    def dfs(vertex):
        if vertex==n:return True
        for col in range(m):
            if valid(vertex, col):
                colors[vertex] = col
                if dfs(vertex+1):
                    return True
                colors[vertex] = -1
        return False

    n = len(mat)
    colors = [-1]*n
    if dfs(0):return "YES"
    return "NO"


mat = [[0,1,0],[1, 0, 1], [0, 1, 0]]
m=3
print(graphColoring(mat, m),True)
mat = [[0,1,0],[1, 0, 1], [0, 1, 0]]
m=1
print(graphColoring(mat, m),False)
