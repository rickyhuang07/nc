class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph = {i: [] for i in range(n)}

        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        path = set()

        def dfs(node):
            if node in path:
                return False

            path.add(node)

            for nbr in graph[node]:
                # Remove the reverse edge so we don't
                # immediately travel back to the node we came from
                graph[nbr].remove(node)

                if not dfs(nbr):
                    return False

            return True

        if len(edges) > n - 1:
            return False

        if not dfs(0):
            return False

        return len(path) == n