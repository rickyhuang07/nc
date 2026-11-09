class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        need = [0] * 26
        for s in s1:   
            need[ord(s) - ord('a')] += 1
        l = 0
        have = [0] * 26
        for i in range (len(s1)):
            have[ord(s2[i]) - ord('a')] += 1
        for r in range (len(s1), len(s2)):
            if need == have:
                return True
            have[ord(s2[l]) - ord('a')] -= 1
            have[ord(s2[r]) - ord('a')] += 1
            l += 1
        return need == have
            
            



            


            