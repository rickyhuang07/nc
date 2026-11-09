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
        start = []
        end = []
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start.sort()
        end.sort()
        ptr1, ptr2 = 0, 0
        while ptr1 < len(start):
            if start[ptr1] < end[ptr2]:
                ptr1 += 1
                count += 1
            else:
                ptr1 += 1
                ptr2 += 1
            res = max(res, count)
        return res

