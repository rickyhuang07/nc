class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for i in range (len(board)):
            for j in range (len(board[i])):
                if board[i][j] == '.':
                    continue
                val = int(board[i][j]) - 1
                if rows[i] & (1 << val):
                    return False
                if cols[j] & (1 << val):
                    return False
                if (1 << val) & squares[(i // 3) * 3 + (j // 3)]:
                    return False
                rows[i] |= (1 << val)
                cols[j] |= (1 << val)
                squares[(i // 3) * 3 + (j // 3)] |= (1 << val)
                
        
        return True