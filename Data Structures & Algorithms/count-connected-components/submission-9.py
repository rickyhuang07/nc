class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        res = 0
        graph = [[] for _ in range (n)]
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in graph[node]:
                if nei in visited:
                    continue
                dfs(nei)
        for i in range (n):
            if i not in visited:
                dfs(i)
                res += 1
        return res
                
                