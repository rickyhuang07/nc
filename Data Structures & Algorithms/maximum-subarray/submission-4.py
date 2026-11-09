class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [[-1] * 2 for _ in range (len(nums))]
        def dfs(i, flag):
            if dp[i][flag] != -1:
                return dp[i][flag]
            if i == len(nums) - 1:
                if flag:
                    return max(0, nums[i])
                return nums[i]
            if flag:
                res = max(0, nums[i] + dfs(i + 1, True))
                dp[i][flag] = res
                return res
            res = max(nums[i] + dfs(i + 1, True), dfs(i + 1, False))
            dp[i][flag] = res
            return res
        return dfs(0, False)