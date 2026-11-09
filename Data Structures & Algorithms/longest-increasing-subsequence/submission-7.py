class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [[-1] * len(nums) for _ in range (len(nums))]
        def dfs(i, j):
            if i == len(nums):
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            res = dfs(i + 1, j)
            if j == -1 or nums[i] > nums[j]:
                res = max(res, 1 + dfs(i + 1, i))
            dp[i][j] = res
            return res

        return dfs(0, -1)
            