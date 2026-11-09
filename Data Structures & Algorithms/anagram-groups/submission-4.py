class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            new = ''.join(sorted(s))
            res[new].append(s)
        return list(res.values())
        
        
        