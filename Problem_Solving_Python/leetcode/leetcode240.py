# could not solve
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n-1
        temp = 0
        while j>=0 and i < m:
            temp = matrix[i][j]
            if matrix[i][j] == target:
                return True
            if target<matrix[i][j]:
                j-=1
            else:
                i+=1
        return False



