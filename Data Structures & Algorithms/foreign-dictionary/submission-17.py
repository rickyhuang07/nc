class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj}
        for i in range (len(words) - 1):
            word1 , word2 = words[i], words[i + 1]
            minLen = min(len(word1), len(word2))
            if word2 == word1[:minLen] and len(word2) < len(word1):
                return ""
            for i in range (minLen):
                if word1[i] != word2[i]:
                    if word2[i] not in adj[word1[i]]:
                        indegree[word2[i]] += 1
                    adj[word1[i]].add(word2[i])
                    break
        res = []
        q = deque()
        for c in indegree:
            if indegree[c] == 0:
                q.append(c)
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