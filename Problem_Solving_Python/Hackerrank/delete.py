def make_board(nums):
    n = len(nums)
    actual_board = []
    board = [['.']*n for _ in range(n)]
    for row, col in enumerate(nums):
        board[row][col] = 'Q'
    for row in board:
        actual_board.append("".join(row))
    return actual_board

def make_all_board(res):
    actual_boards = []
    for nums in res:
        actual_boards.append(make_board(nums))
    return actual_boards

print(make_all_board([[1,3,0,2],[2,0,3,1]]))