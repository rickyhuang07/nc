class DSU:
    def __init__(self, n):
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        if self.Size[px] >= self.Size[py]:
            self.Parent[py] = px
            self.Size[px] += self.Size[py]
        else:
            self.Parent[px] = py
            self.Size[py] += self.Size[px]
        return True


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        dsu = DSU(rows * cols)
        def index(r, c):
            return r * cols + c
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                for nr, nc in directions:
                    nr += r
                    nc += c
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == "0" or grid[r][c] == "0":
                        continue
                    if dsu.union(index(r, c), index (nr, nc)):
                        islands -= 1
        return islands

        