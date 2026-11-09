class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range (n)]
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
        visited = set()
        def dfs(node, parent):
            #cycle detection
            if node in visited:
                return False
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        if not dfs(0, -1):
            return False
        return len(visited) == n
        
