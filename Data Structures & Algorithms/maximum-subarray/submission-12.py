class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[n-1]
        dp = [[-1] * 2 for _ in range (n)]
        dp[n-1][0] = nums[n-1]
        dp[n-1][1] = max(nums[n-1], 0)
        for i in range (n-2, -1, -1):
            for j in range (2):
                dp[i][0] = max(nums[i] + dp[i+1][1], nums[i])
                dp[i][1] = max(0, dp[i][0])
                res = max(res, dp[i][0])
        return res