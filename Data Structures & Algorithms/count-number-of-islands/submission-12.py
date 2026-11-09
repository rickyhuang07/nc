class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        res = 0
        
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            while q:
                x, y = q.popleft()
                if x - 1 >= 0 and grid[x-1][y] == "1" and (x - 1, y) not in visited:
                    q.append((x-1, y))
                    visited.add((x - 1, y))
                if x + 1 < rows and grid[x + 1][y] == "1" and (x + 1, y) not in visited:
                    q.append((x + 1, y))
                    visited.add((x + 1, y))
                if y - 1 >= 0 and grid[x][y - 1] == "1" and (x, y - 1) not in visited:
                    q.append((x, y - 1))
                    visited.add((x, y - 1))
                if y + 1 < cols and grid[x][y + 1] == "1" and (x, y + 1) not in visited:
                    q.append((x, y + 1))
                    visited.add((x, y + 1))
            

        for i in range (rows):
            for j in range (cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    res += 1
        return res
                