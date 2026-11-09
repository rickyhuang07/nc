class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        lengths = defaultdict(int)
        for num in nums:
            if not lengths[num]:
                lengths[num] = 1 + lengths[num - 1] + lengths[num + 1]
                if lengths[num - 1]:
                    lengths[num - lengths[num - 1]] = lengths[num]
                if lengths[num + 1]:
                    lengths[num + lengths[num + 1]] = lengths[num]
            longest = max (longest, lengths[num])
        return longest



        