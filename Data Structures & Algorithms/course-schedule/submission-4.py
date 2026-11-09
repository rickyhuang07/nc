class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range (numCourses)}
        for crs, req in prerequisites:
            preMap[crs].append(req)
        path = set()
        def dfs(node):
            if node in path:
                return False
            if preMap[node] == []:
                return True
            path.add(node)
            for prereq in preMap[node]:
                if not dfs(prereq):
                    return False
            path.remove(node)
            preMap[node] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True