from typing import List


class Position:

    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col


class Solution:

    # def solveNQueens(self, n: int) -> List[List[str]]:

    def solveNQueensUtility(self, ROW: int, n: int, positions: List[Position]):
        if ROW == n:
            return True
        for col in range(n):
            isSafe = True
            for queen in range(ROW):
                if positions[queen].col == col or positions[queen].row == queen or positions[queen].col - positions[
                    queen].row == col - ROW or positions[queen].col + positions[queen].row == col + ROW:
                    isSafe = False
                    break
            if isSafe:
                positions.append(Position(ROW, col))
                if self.solveNQueensUtility(ROW + 1, n, positions):
                    return True
        return False
