mat = [
    [0,1,2,3,4,5,6,7],
    [8,9,10,11,12,13,14,15],
    [16,17,18,19,20,21,22,23]
]

mat = [
    [0, 8, 16],
    [1, 9, 17],
    [2, 10, 18],
    [3, 11, 19],
    [4, 12, 20],
    [5, 13, 21],
    [6, 14, 22],
    [7, 15, 23]
       ]

r = len(mat)
c = len(mat[0])

# newmat = [[0]*r for _ in range(c)]
# for i in range(c):
#     for j in range(r):
#         newmat[i][j] = mat[j][i]
# print(newmat)
# for i in range(c-r):
#     a = [row[i:r+i] for row in mat]
#     print(a)

for i in range(abs(c-r)):
    a = mat[i:i+c]
    print(a)

print('\n\n')
print([mat[0:3]])