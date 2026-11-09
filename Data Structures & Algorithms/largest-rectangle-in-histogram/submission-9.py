class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        pre = [0] * len(heights)
        post = [0] * len(heights)
        stack = []
        for i in range (len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                pre[i] = i - stack[-1] - 1
            else:
                pre[i] = i
            stack.append(i)
        stack = []
        for i in range (len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                post[i] = stack[-1] - i - 1
            else:
                post[i] = len(heights) - 1 - i
            stack.append(i)

        res = 0
        for i in range (len(heights)):
            res = max(res, (pre[i] + post[i] + 1) * heights[i])
        return res


        


        