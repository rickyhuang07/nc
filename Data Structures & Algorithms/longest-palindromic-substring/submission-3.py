class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        maxlength = 0
        def expandOdd(idx):
            left, right = idx, idx
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]

        def expandEven(l, r):
            left = l
            right = r
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]

        for i in range (0, len(s)):
            if len(expandEven(i - 1, i)) > maxlength:
                res = expandEven(i - 1, i)
                maxlength = len(res)
            if len(expandOdd(i)) > maxlength:
                res = expandOdd(i)
                maxlength = len(res)
            
        return res

