class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range (numCourses)}
        for a, b in prerequisites:
            preMap[a].append(b)
        path = set()
        def dfs(course):
            if course in path:
                return False
            if preMap[course] == []:
                return True
            path.add(course)
            for req in preMap[course]:
                if not dfs(req):
                    return False
            path.remove(course)
            preMap[course] = []
            return True


            
        for crse in preMap:
            if not dfs(crse):
                return False
        return True