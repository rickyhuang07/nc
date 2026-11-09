class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        convert = bin(n)
        binary = convert[2:]
        for digit in binary:
            if digit == '1':
                res += 1
        return res
        