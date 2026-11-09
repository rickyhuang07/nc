class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        leastidx = l
        
        def bsearch(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        if bsearch(0, leastidx - 1) != -1:
            return bsearch(0, leastidx - 1)
        else:
            return bsearch(leastidx, len(nums) - 1)

        
        

        