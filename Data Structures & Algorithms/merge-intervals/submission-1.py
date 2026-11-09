class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        for i in range (1, len(intervals)):
            if intervals[i][0] <= intervals[i-1][1]:
                intervals[i][0] = intervals[i-1][0]
                intervals[i][1] = max(intervals[i][1], intervals[i-1][1])
            else:
                res.append(intervals[i-1])
        res.append(intervals[len(intervals)-1])
        return res
