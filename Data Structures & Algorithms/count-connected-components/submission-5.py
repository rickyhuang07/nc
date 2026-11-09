class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        visited = set()
        path = set()

        premap = {i: [] for i in range(n)}

        for e1, e2 in edges:
            premap[e1].append(e2)
            premap[e2].append(e1)

        def dfs(node, parent):
            if node in path:
                return

            visited.add(node)
            path.add(node)

            for nei in premap[node]:
                if nei == parent or nei in visited:
                    continue
                dfs(nei, node)

            path.remove(node)

        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                res += 1

        return res