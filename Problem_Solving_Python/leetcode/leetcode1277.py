rec_mat = [
    [0,1,2,3,4,5,6,7],
    [8,9,10,11,12,13,14,15],
    [16,17,18,19,20,21,22,23]
]

rec_mat = [
    [0, 8, 16],
    [1, 9, 17],
    [2, 10, 18],
    [3, 11, 19],
    [4, 12, 20],
    [5, 13, 21],
    [6, 14, 22],
    [7, 15, 23]
       ]


def rectangle_to_all_possible_square_rec_matrix(rec_mat):
    sq_matrices = []
    r = len(rec_mat)
    c = len(rec_mat[0])
    if c > r:
        new_rec_mat = [[0] * r for _ in range(c)]
        for i in range(c):
            for j in range(r):
                new_rec_mat[i][j] = rec_mat[j][i] # transpose matrix
        rec_mat = new_rec_mat
        c, r = r, c # swap r and c in transpose matrix
    for i in range(abs(c - r)):
        sq_matrices.append(rec_mat[i:i + c])
    return sq_matrices


sq_matrices = rectangle_to_all_possible_square_rec_matrix(rec_mat)
for matrix in sq_matrices:
    print(matrix)