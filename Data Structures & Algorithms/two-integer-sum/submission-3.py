class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        flist = []
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    flist.append(i)
                    flist.append(j)
                    return flist

        