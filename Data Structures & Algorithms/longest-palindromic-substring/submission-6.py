class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxidx = -1
        maxlen = 0
        n = len(s)
        dp = [[False] * n for _ in range (n)]
        for i in range (n - 1, -1, -1):
            for j in range (i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if j - i + 1 > maxlen:
                        maxlen = j - i + 1
                        maxidx = i
        return s[maxidx:maxidx + maxlen]