"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldToNew = {}
        def dfs(node):
            if node not in oldToNew:
                new = Node(node.val)
                oldToNew[node] = new
                for n in node.neighbors:
                    new.neighbors.append(dfs(n))
                return new

            else:
                return oldToNew[node]
        
        return dfs(node)



        