class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range (len(board)):
            visited = set()
            for j in range (len(board[i])):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in visited:
                    visited.add(board[i][j])
                else:
                    return False

        for i in range (len(board[0])):
            visited = set()
            for j in range (len(board)):
                if board[j][i] == ".":
                    continue
                if board[j][i] not in visited:
                    visited.add(board[j][i])
                else:
                    return False
        
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True