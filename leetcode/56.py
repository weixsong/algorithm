# -*- encoding: utf-8 -*-
'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        if len(intervals) == 0:
            return []
        
        intervals = sorted(intervals, key=lambda x: x.start)

        res = [intervals[0]]

        for interval in intervals:
            last = res[-1]

            if interval.start <= last.end:
                last.end = max(interval.end, last.end)
            else:
                res.append(interval)

        return res

if __name__ == '__main__':
    i1 = Interval(1, 4)
    i2 = Interval(0, 4)

    so = Solution()
    res = so.merge([i1, i2])

    for item in res:
        print [item.start, item.end]

