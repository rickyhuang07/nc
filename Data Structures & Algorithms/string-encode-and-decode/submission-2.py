class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes = []
        for s in strs:
            sizes.append(str(len(s)))
            sizes.append(',')
        sizes.append('#')
        sizes.extend(strs)
        return ''.join(sizes)
        

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, flist = [], []
        i = 0
        while s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            sizes.append(int(s[i:j]))
            i = j + 1
        i += 1
        for sz in sizes:
            flist.append(s[i:i + sz])
            i += sz
        return flist
            

        
