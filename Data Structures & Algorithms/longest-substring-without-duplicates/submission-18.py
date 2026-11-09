class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = set()
        res = 0
        left = 0
        for r in range (len(s)):
            while s[r] in cur:
                cur.remove(s[left])
                left += 1
            cur.add(s[r])
            res = max(res, r - left + 1)
        return res