def expandAroundCenter(i, s):
    idx = i / 2
    if i % 2 == 0:
        cur = s[int(idx)]
        left, right = int(idx), int(idx)
        while left >= 1 and right < len(s) - 1:
            left -= 1
            right += 1
            if s[left] == s[right]:
                cur = s[left:right + 1]
            else:
                break
    else:
        cur = ""
        left, right = math.floor(idx), math.ceil(idx)
        while s[left] == s[right]:
            cur = s[left: right + 1]
            if left >= 1 and right < len(s) - 1:
                left -= 1
                right += 1
            else:
                break
    return cur


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range (2 * len(s) - 1):
            pal = expandAroundCenter(i, s)
            if len(pal) > len(longest):
                longest = pal
        return longest
        
    