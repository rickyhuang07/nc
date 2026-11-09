class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        flist = []
        flag1 = False
        flag2 = False
        prod = 1
        for num in nums:
            if num != 0:
                prod*= num
            elif not flag1 and num == 0:
                flag1 = True
            elif not flag2 and num == 0:
                flag2 = True
        for num in nums:
            if flag2:
                flist.append(0)
            elif flag1:
                if num == 0:
                    flist.append(prod)
                else:
                    flist.append(0)
            elif not flag1:
                flist.append(int(prod/num))

        return flist
        