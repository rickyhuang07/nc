class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(filter(str.isalnum, s))
        fstr = string.lower()
        for i in range (0, math.ceil(len(fstr) / 2)):
            if fstr[i] != fstr[len(fstr) - i - 1]:
                return False
        return True  