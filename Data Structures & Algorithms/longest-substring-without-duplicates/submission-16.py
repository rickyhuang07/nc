class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we can use a sliding window approach
        substr = set()
        res = 0
        left = 0
        for i in range (len(s)):
            while s[i] in substr:
                substr.remove(s[left])
                left += 1
            substr.add(s[i])
            res = max(res, i - left + 1)
        return res
            
