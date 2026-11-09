class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            array = [0] * 26
            for c in s:
                array[ord(c)-ord('a')] += 1
            res[tuple(array)].append(s)
        return list(res.values())
