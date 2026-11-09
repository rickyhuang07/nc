class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 1
        hash = set()
        if not nums:
            return 0
        for num in nums:
            hash.add(num)
        for num in hash:
            if num - 1 in hash:
                streak = 2
                while num + streak - 1 in hash:
                    streak += 1
                longest = max (streak, longest)
        return longest



        