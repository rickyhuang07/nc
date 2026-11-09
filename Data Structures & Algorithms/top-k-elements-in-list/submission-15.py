class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        flist = []
        listfinal = []
        count = {}
        for i in range (len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)
        for key, value in count.items():
           # print ([key, value])
            listfinal.append([value, key])
        listfinal.sort()
        for i in range (len(listfinal) - 1, len(listfinal) - k - 1, -1):
            flist.append(listfinal[i][1])
        return flist


        