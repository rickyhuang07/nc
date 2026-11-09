class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a = set()
        nums.sort()
        for i in range (len(nums) - 2):
            curr = nums[i]
            ptr1 = i + 1
            ptr2 = len(nums) - 1
            while ptr1 < ptr2:
                if curr + nums[ptr1] + nums[ptr2] == 0:
                    a.add((curr, nums[ptr1], nums[ptr2]))
                    ptr1 += 1
                    ptr2 -= 1
                elif curr + nums[ptr1] + nums[ptr2] < 0:
                    ptr1 += 1
                else:
                    ptr2 -= 1
        return [list(t) for t in a]