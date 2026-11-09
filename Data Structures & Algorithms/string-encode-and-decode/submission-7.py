class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append(',')
            res.append(s)
        res.append('#')
        return "".join(res)
        

    def decode(self, s: str) -> List[str]:
        flist = []
        if not s:
            return []
        i = 0
        while s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            length = int(s[i:j])
            flist.append(s[j+1: j+1+length])
            i = j + 1 + length
        return flist

            

        
