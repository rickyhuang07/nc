class Solution:
    def numDecodings(self, s: str) -> int:
        dp1 = [-1] * len(s)
        dp2 = [-1] * len(s)
        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if dp1[i] == -1:
                res = dfs(i + 1)
                dp1[i] = res
            else:
                res = dp1[i]
            if i < len(s) - 1:
                if 10 <= int(s[i:i+2]) <= 26:
                    if dp2[i] == -1:
                        add = dfs(i + 2)
                        res += add
                        dp2[i] = add
                    else:
                        res += dp2[i]
            return res
        return dfs(0)
    
        