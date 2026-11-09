class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        finished = 0
        for a, b in prerequisites:
            preMap[b].append(a)
            indegree[a] += 1
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        while q:
            node = q.popleft()
            finished += 1
            for el in preMap[node]:
                indegree[el] -= 1
                if indegree[el] == 0:
                    q.append(el)
        if finished == numCourses:
            return True
        return False
