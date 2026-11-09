class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rows, cols = [False] * ROWS, [False] * COLS
        for i in range (ROWS):
            for j in range (COLS):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
        for r in range(ROWS):
            if rows[r]:
                for i in range (COLS):
                    matrix[r][i] = 0
        for c in range(COLS):
            if cols[c]:
                for i in range (ROWS):
                    matrix[i][c] = 0
    
    
                

        
        