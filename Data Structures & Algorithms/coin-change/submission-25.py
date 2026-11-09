class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        def dfs(total):
            if total == 0:
                return 0
            if dp[total] != -1:
                return dp[total]
            res = 1e9
            for c in coins:
                if total - c >= 0:
                    res = min(res, 1 + dfs(total - c))
            dp[total] = res
            return res
        final = dfs(amount)
        if final == 1e9:
            return -1
        return final
            