class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        lp, rp = 0, len(heights) - 1
        while lp < rp:
            maxarea = max(maxarea, (rp - lp)* min(heights[lp], heights[rp]))
            if heights[lp] <= heights[rp]:
                lp += 1
            else:
                rp -= 1
        return maxarea
                

        