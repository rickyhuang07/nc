class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        visited = [[False for _ in range (col)] for _ in range (row)]

        def dfs (r, c, idx):
            if idx == len(word):
                return True
            if r < 0 or c < 0 or r >= row or c >= col or board[r][c] != word[idx] or visited[r][c]:
                return False
            visited[r][c] = True
            res = dfs(r + 1, c, idx + 1) or dfs(r - 1, c, idx + 1) or dfs(r, c + 1, idx + 1) or dfs(r, c - 1, idx + 1)
            visited[r][c] = False
            return res

        for i in range (row):
            for j in range (col):
                if dfs(i, j, 0):
                    return True
        return False
