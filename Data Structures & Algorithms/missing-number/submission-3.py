class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numbers = set()
        for i in range (len(nums) + 1):
            numbers.add(i)
        for num in nums:
            numbers.remove(num)
        for num in numbers:
            return num