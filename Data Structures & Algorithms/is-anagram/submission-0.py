class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = list(s)
        tlist = list(t)
        slist.sort()
        tlist.sort()
        if len(slist) != len(tlist):
            return False
        else:
            for i in range (len(slist)):
                if slist[i] != tlist[i]:
                    return False
        return True

        
        

        