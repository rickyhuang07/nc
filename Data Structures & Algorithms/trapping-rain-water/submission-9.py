class Solution:
    def trap(self, height: List[int]) -> int:
        prefix , suffix = [-1] * len(height), [-1] * len(height)
        for i in range (1, len(height)):
            prefix[i] = max(prefix[i - 1], height[i - 1])
            suffix[len(height) - i - 1] = max(suffix[len(height) - i], height[len(height) - i])
        total = 0
        for i in range (1, len(height) - 1):
            total += max(0, min(prefix[i], suffix[i]) - height[i])
        return total
