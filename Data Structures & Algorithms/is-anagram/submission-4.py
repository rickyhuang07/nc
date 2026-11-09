class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = list(s)
        tlist = list(t)
        slist.sort()
        tlist.sort()
        return slist == tlist

        
        

        