class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range (numCourses)}
        indegree = [0] * numCourses
        taken = 0
        q = deque()
        for crs, req in prerequisites:
            preMap[req].append(crs)
            indegree[crs] += 1
        for idx in range (numCourses):
            if indegree[idx] == 0:
                q.append(idx)
        while q:
            node = q.popleft()
            taken += 1
            for nei in preMap[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return taken == numCourses
            
        

