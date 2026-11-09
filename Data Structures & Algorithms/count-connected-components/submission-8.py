class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        visited = set()
        premap = {i: [] for i in range(n)}

        for e1, e2 in edges:
            premap[e1].append(e2)
            premap[e2].append(e1)

        def dfs(node):
            visited.add(node)
            for nei in premap[node]:
                if nei not in visited:
                    dfs(nei)

        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res