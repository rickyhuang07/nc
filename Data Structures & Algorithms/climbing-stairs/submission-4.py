class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        one = 1
        two = 2
        cur = 0
        for i in range (3, n + 1):
            cur = one + two
            one = two
            two = cur
        return cur
            
