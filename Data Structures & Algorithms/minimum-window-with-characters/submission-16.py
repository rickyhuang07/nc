class Solution:
    def minWindow(self, s: str, t: str) -> str:
        targ, window = {}, {}
        for c in t:
            targ[c] = 1 + targ.get(c, 0)
        have, needed = 0, len(targ)
        shortest = len(s) + 1
        shortstring = [-1, -1]
        l = 0
        for r in range (len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in targ and window[s[r]] == targ[s[r]]:
                have += 1
            while have == needed:
                if r - l + 1 < shortest:
                    shortest = r - l + 1
                    shortstring = [l, r]
                window[s[l]] -= 1
                if s[l] in targ and window[s[l]] < targ[s[l]]:
                    have -= 1
                l += 1

        return s[shortstring[0]:shortstring[1] + 1]
        
            

            
