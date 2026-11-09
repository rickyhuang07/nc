class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        rows = len(heights)
        cols = len(heights[0])
        pac, atl = set(), set()
        def bfs(r, c, visit):
            q = [(r, c)]
            for i, j in q:
                if (i, j) in visit or i < 0 or j < 0 or i >= rows or j >= cols: 
                    continue
                visit.add((i, j))
                if i + 1 < rows and heights[i + 1][j] >= heights[i][j]:
                    q.append((i + 1, j))
                if i - 1 >= 0 and heights[i - 1][j] >= heights[i][j]:
                    q.append((i - 1, j))
                if j + 1 < cols and heights[i][j + 1] >= heights[i][j]:
                    q.append((i, j + 1))
                if j - 1 >= 0 and heights[i][j - 1] >= heights[i][j]:
                    q.append((i, j - 1))
                

        for r in range (rows):
            bfs(r, 0, pac)
            bfs(r, cols - 1, atl)

        for c in range (cols):
            bfs(0, c, pac)
            bfs(rows - 1, c, atl)
        
        for r in range (rows):
            for c in range (cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res