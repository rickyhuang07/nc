class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [None] * (len(nums))
        def dfs(idx):
            if dp[idx] is not None:
                return dp[idx]
            if idx >= len(nums) - 1:
                return True
            for i in range (1, nums[idx] + 1):
                if dfs(idx + i):
                    dp[idx] = True
                    return True
            dp[idx] = False
            return False
        return dfs(0)