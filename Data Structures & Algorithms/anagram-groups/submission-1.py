class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            sortedstr = ''.join(sorted(string))
            result[sortedstr].append(string)
        return list(result.values())
