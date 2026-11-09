class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(idx, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or idx >= len(nums):
                return
            cur.append(nums[idx])
            dfs(idx, cur, total + nums[idx])
            cur.pop()
            dfs(idx + 1, cur, total)
        dfs(0, [], 0)
        return res

        

