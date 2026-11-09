class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range (len(temperatures) - 1, -1, -1):
            j = i + 1
            while j < len(temperatures) and temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    break
                else:
                    j += res[j]
            if j < len(temperatures) and temperatures[j] > temperatures[i]:
                res[i] = j - i
        return res


                