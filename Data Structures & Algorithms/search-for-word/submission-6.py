class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word or not board:
            return False
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        def dfs(x, y, idx):
            if idx == len(word):
                return True
            if (x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or word[idx]!= board[x][y] or visited[x][y]):
                return False
            visited[x][y] = True
            res = (dfs(x + 1, y, idx + 1) or dfs(x - 1, y, idx + 1) or dfs(x, y + 1, idx + 1) or dfs(x, y - 1, idx + 1))
            visited[x][y] = False
            return res
            


        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
