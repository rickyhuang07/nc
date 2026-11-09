class Solution:
    def getSum(self, a: int, b: int) -> int:
        bitmask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while b:
            carry = (a & b) << 1
            a = (a ^ b) & bitmask
            b = carry & bitmask
        return a if a <= max_int else ~ (a ^ bitmask)