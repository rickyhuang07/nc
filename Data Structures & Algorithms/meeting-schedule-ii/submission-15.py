"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        count = 0
        res = 0
        times = []
        for interval in intervals:
            times.append((interval.start, 1))
            times.append((interval.end, -1))
        times.sort(key = lambda x : (x[0], x[1]))
        for time in times:
            if time[1] == 1:
                count += 1
            if time[1] == -1:
                count -= 1
            res = max(res, count)
        return res

