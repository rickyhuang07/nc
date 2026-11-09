class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        adj= {c: set() for w in words for c in w}
        for i in range (n - 1):
            s1, s2 = words[i], words[i+1]
            minLen = min(len(s1), len(s2))
            if s1[:minLen] == s2[:minLen] and len(s1) > len(s2):
                return ""
            for j in range (minLen):
                if s1[j] != s2[j]:
                    adj[s1[j]].add(s2[j])
                    break
        res = []
        visited = {}
        def dfs(char):
            if char in visited:
                return visited[char]
            visited[char] = True
            for nei in adj[char]:
                if dfs(nei):
                    return True
            visited[char] = False
            res.append(char)
            return False
        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)
        
