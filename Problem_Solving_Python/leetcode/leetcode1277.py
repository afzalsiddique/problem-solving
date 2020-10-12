from typing import List


class Solution:
    memo = {}
    count = 0
    matrix = []

    def countSquares(self, matrix: List[List[int]]) -> int:
        no_row = len(matrix) - 1
        no_col = len(matrix[0]) - 1
        if no_row == no_col:
            self.matrix = matrix
            self.one_zero_matrix_to_true_false_matrix(matrix)
            self.helper(0, no_row, 0, no_col)
            return self.count
        else:
            sq_matrices = self.rectangle_to_all_possible_square_matrices(matrix)
            for mat in sq_matrices:
                no_of_row = len(mat) - 1
                no_of_col = len(mat[0]) - 1
                self.matrix = mat
                self.one_zero_matrix_to_true_false_matrix(mat)
                self.helper(0, no_of_row, 0, no_of_col)
            return self.count

    def helper(self, r1, r2, c1, c2):
        if r1 == r2 and c1 == c2:
            return self.matrix[r1][c1]
        if (r1, r2, c1, c2) in self.memo:
            return self.memo[(r1, r2, c1, c2)]

        # print(r1,r2,c1,c2)
        first = self.helper(r1 + 1, r2, c1 + 1, c2)
        second = self.helper(r1 + 1, r2, c1, c2 - 1)
        third = self.helper(r1, r2 - 1, c1 + 1, c2)
        fourth = self.helper(r1, r2 - 1, c1, c2 - 1)
        temp = first and second and third and fourth
        if temp:
            self.count += 1
        self.memo[(r1, r2, c1, c2)] = temp
        return self.memo[(r1, r2, c1, c2)]

    def one_zero_matrix_to_true_false_matrix(self, matrix):
        no_row = len(matrix)
        no_col = len(matrix[0])
        for i in range(no_row):
            for j in range(no_col):
                if self.matrix[i][j]:
                    self.matrix[i][j] = True
                    self.count += 1
                else:
                    self.matrix[i][j] = False

    def rectangle_to_all_possible_square_matrices(self, rec_mat):
        sq_matrices = []
        r = len(rec_mat)
        c = len(rec_mat[0])
        if c > r:
            new_rec_mat = [[0] * r for _ in range(c)]
            for i in range(c):
                for j in range(r):
                    new_rec_mat[i][j] = rec_mat[j][i]  # transpose matrix
            rec_mat = new_rec_mat
            c, r = r, c  # swap r and c in transpose matrix
        for i in range(abs(c - r)):
            sq_matrices.append(rec_mat[i:i + c])
        return sq_matrices

# rec_mat = [
#     [0,1,2,3,4,5,6,7],
#     [8,9,10,11,12,13,14,15],
#     [16,17,18,19,20,21,22,23]
# ]
#
# rec_mat = [
#     [0, 8, 16],
#     [1, 9, 17],
#     [2, 10, 18]
#        ]


# rec_mat = [
#     [0, 8, 16],
#     [1, 9, 17],
#     [2, 10, 18],
#     [3, 11, 19],
#     [4, 12, 20],
#     [5, 13, 21],
#     [6, 14, 22],
#     [7, 15, 23]
#        ]


#
#
# sq_matrices = rectangle_to_all_possible_square_matrices(rec_mat)
# for matrix in sq_matrices:
#     print(matrix)


# mat = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16]
# ]
