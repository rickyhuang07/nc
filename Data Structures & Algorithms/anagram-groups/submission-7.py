class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            curr = [0] * 26
            for c in s:
                curr[ord(c) - ord('a')] += 1
            res[tuple(curr)].append(s)
        return list(res.values())


        
        
        