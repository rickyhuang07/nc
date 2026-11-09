class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums):
            new_list = sorted(nums)
            recent = new_list[0] - 1
            for i in range (len(new_list)):
                if recent == new_list[i]:
                    return True
                else:
                    recent = new_list[i]
            return False
        else:
            return False
            
               
            
        