class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        for i in range (len(words) - 1):
            word1 , word2 = words[i], words[i + 1]
            minLen = min(len(word1), len(word2))
            if word2 == word1[:minLen] and len(word2) < len(word1):
                return ""
            for i in range (minLen):
                if word1[i] != word2[i]:
                    adj[word1[i]].add(word2[i])
                    break
        visited = {}
        res = []
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

