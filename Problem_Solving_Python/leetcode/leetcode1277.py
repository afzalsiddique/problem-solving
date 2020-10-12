# rec_mat = [
#     [0,1,2,3,4,5,6,7],
#     [8,9,10,11,12,13,14,15],
#     [16,17,18,19,20,21,22,23]
# ]
#
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
# def rectangle_to_all_possible_square_matrices(rec_mat):
#     sq_matrices = []
#     r = len(rec_mat)
#     c = len(rec_mat[0])
#     if c > r:
#         new_rec_mat = [[0] * r for _ in range(c)]
#         for i in range(c):
#             for j in range(r):
#                 new_rec_mat[i][j] = rec_mat[j][i] # transpose matrix
#         rec_mat = new_rec_mat
#         c, r = r, c # swap r and c in transpose matrix
#     for i in range(abs(c - r)):
#         sq_matrices.append(rec_mat[i:i + c])
#     return sq_matrices
#
#
# # sq_matrices = rectangle_to_all_possible_square_matrices(rec_mat)
# # for matrix in sq_matrices:
# #     print(matrix)
#
#
#
#

# mat = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16]
# ]

class Solution:
    mat = [
        [False,False,True, True],
        [True,True, True,True],
        [True, True, True,True],
        [True,True,True,True],
    ]
    memo = {}
    count = 0
    def break_matrix(self,r1,r2,c1,c2):
        if r1==r2 and c1==c2:
            return self.mat[r1][c1]
        if (r1,r2,c1,c2) in self.memo:
            return self.memo[(r1,r2,c1,c2)]

        # print(r1,r2,c1,c2)
        first = self.break_matrix(r1+1,r2,c1+1,c2)
        second = self.break_matrix(r1+1,r2,c1,c2-1)
        third = self.break_matrix(r1,r2-1,c1+1,c2)
        fourth = self.break_matrix(r1,r2-1,c1,c2-1)
        temp = first and second and third and fourth
        if temp:
            self.count+=1
        self.memo[(r1,r2,c1,c2)] = temp
        return self.memo[(r1,r2,c1,c2)]

solution = Solution()
solution.break_matrix(0,3,0,3)
print(solution.memo)
print(solution.count)