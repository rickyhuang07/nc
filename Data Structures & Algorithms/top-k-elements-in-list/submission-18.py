class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        flist = []
        count = {}
        freq = [[] for i in range (len(nums) + 1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for key, value in count.items():
            freq[value].append(key)
        for i in range (len(freq) - 1, 0, -1):
            for j in range(len(freq[i])):
                flist.append(freq[i][j])
                if len(flist) == k:
                    return flist
        


        