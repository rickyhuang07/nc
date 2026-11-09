class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        res = []
        pac, atl = set(), set()
        def dfs(r, c, visit, val):
            if r < 0 or c < 0 or r >= rows or c >= cols or heights[r][c] < val or (r, c) in visit:
                return False
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        
        for r in range (rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        
        for i in range (rows):
            for j in range (cols):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        return res

        
