class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [None] * len(s)      
        def dfs(i):
            if i == len(s):
                return True
            for word in wordDict:
                if s[i:i + len(word)] == word:
                    if dp[i] != None:
                        return dp[i]
                    if dfs(i + len(word)):
                        dp[i] = True
                        return True
            dp[i] = False
            return False

        return dfs(0)