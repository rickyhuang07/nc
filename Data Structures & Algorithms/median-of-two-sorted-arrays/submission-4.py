class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        half = (len(nums1) + len(nums2)) // 2
        if len(nums1) > len(nums2):
            temp = nums1
            nums1 = nums2
            nums2 = temp
        left, right = 0, len(nums1)
        while left <= right:
            mid = (left + right) // 2
            j = half - mid
            left1 = nums1[mid - 1] if mid > 0 else float('-inf')
            right1 = nums1[mid] if mid < len(nums1) else float('inf')
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < len(nums2) else float('inf')
            if left1 > right2:
                right = mid - 1
            elif left2 > right1:
                left = mid + 1
            else:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return min(right1, right2)
            
        
            


            

        
