class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #cycle detection
        graph = {i:[] for i in range (n)}
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        path = set()
        def dfs(node, parent):
            if node in path:
                return False
            path.add(node)
            for nbrs in graph[node]:
                if nbrs == parent:
                    continue
                if not dfs(nbrs, node):
                    return False
            return True
        if len(edges) > n - 1:
            return False
        if not dfs(0, -1):
            return False
        if len(path) != n:
            return False
        return True