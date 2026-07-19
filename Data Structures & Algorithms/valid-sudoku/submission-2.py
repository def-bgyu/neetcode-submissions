class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        for row in board:
            seen_row = set()
            for num in row:
                if num == '.':
                    continue
                if num in seen_row:
                    return False
                else:
                    seen_row.add(num)

        for col in range(9):
            seen_column = set()
            for row in board:
                num = row[col]
                if num == '.':
                    continue
                if num in seen_column:
                    return False
                else:
                    seen_column.add(num)

        for grid in range(9):
            seen_grid = set()
            for i in range(3):
                for j in range(3):
                    row = (grid // 3) *3 + i
                    col = (grid % 3) *3 + j
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in seen_grid:
                        return False
                    else:
                        seen_grid.add(board[row][col])
        return True

        