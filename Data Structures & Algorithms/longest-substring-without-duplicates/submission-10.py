class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        cset = set()
        left = 0
        for right in range (len(s)):
            while s[right] in cset:
                cset.remove(s[left])
                left += 1
            cset.add(s[right])
            longest = max(longest, right - left + 1)
            
        return longest


            
        