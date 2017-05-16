# -*- encoding: utf-8 -*-
'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
'''

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    '''
    O(nlogn)
    '''
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        
        intervals.append(newInterval)

        intervals = sorted(intervals, key=lambda x: x.start)

        res = [intervals[0]]

        for interval in intervals:
            last = res[-1]

            if interval.start <= last.end:
                last.end = max(interval.end, last.end)
            else:
                res.append(interval)

        return res

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    '''
    O(n)
    '''
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        
        l, r = 0, len(intervals) - 1
        while l <= r:
            mid = l + (r - l) / 2
            if intervals[mid].start == newInterval.start:
                l = mid
                break
            if intervals[mid].start > newInterval.start:
                r = mid - 1
            else:
                l = mid + 1

        intervals.insert(l, newInterval)

        res = [intervals[0]]

        for interval in intervals:
            last = res[-1]

            if interval.start <= last.end:
                last.end = max(interval.end, last.end)
            else:
                res.append(interval)

        return res







