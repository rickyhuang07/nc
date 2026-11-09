class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxstreak = 1
        streak = 1
        if not nums:
            return 0
        single = list(dict.fromkeys(nums))
        single.sort()
        for i in range (1, len(single)):
            if single[i] == 1 + single[i-1]:
                streak += 1
            else:
                maxstreak = max(maxstreak, streak)
                streak = 1
        maxstreak = max(maxstreak, streak)
        return maxstreak



        