class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        adj= {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj}
        for i in range (n - 1):
            s1, s2 = words[i], words[i+1]
            minLen = min(len(s1), len(s2))
            if s1[:minLen] == s2[:minLen] and len(s1) > len(s2):
                return ""
            for j in range (minLen):
                if s1[j] != s2[j]:
                    if s2[j] not in adj[s1[j]]:
                        adj[s1[j]].add(s2[j])
                        indegree[s2[j]] += 1
                    break
        q = deque()
        res = []
        for key in indegree:
            if indegree[key] == 0:
                q.append(key)
        while q:
            node = q.popleft()
            res.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        if len(indegree) != len(res):
            return ""
        return "".join(res)


        
