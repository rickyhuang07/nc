class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0" or (r, c) in visited:
                return
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c) 
            dfs(r, c + 1) 
            dfs(r, c - 1)
            
            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    res += 1
        return res

        