class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [None] * (len(nums) * 2)
        def dfs(idx):
            if dp[idx] is not None:
                return dp[idx]
            if idx == len(nums) - 1:
                return True
            if idx >= len(nums):
                return False
            res = False
            for i in range (1, nums[idx] + 1):
                res = dfs(idx + i) or res
            dp[idx] = res
            return res
        return dfs(0)
