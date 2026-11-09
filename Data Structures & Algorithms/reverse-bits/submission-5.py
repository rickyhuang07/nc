class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        binary = bin(n)[2:].zfill(32)
        for i in range (len(binary)-1, -1, -1):
            if binary[i] == '1':
                res += 2 ** i
        return res
