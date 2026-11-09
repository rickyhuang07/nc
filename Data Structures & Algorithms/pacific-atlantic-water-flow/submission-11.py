class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        rows = len(heights)
        cols = len(heights[0])
        visited = set()
        flag1, flag2 = False, False
        def dfs(r, c, val):
            nonlocal flag1, flag2
            if r < 0 or c < 0:
                flag1 = True
                return 
            if r >= rows or c >= cols:
                flag2 = True
                return
            new = heights[r][c]
            if new > val or (r, c) in visited:
                return
            visited.add((r, c))
            dfs(r + 1, c, new)
            dfs(r - 1, c, new)
            dfs(r, c + 1, new)
            dfs(r, c - 1, new)
            return flag1 and flag2

        for r in range (rows):
            for c in range (cols):
                flag1, flag2 = False, False
                if dfs(r, c, heights[r][c]):
                    res.append([r, c])
                visited.clear()
        return res

        # [1, 2, 2, 3, 5]
        # [3, 2, 3, 4, 4]
        # [2, 4, 5, 3, 1]
        # [6, 7, 1, 4, 5]
        # [5, 1, 1, 2, 4]
