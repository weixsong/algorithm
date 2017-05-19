#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

add(1)
add(2)
findMedian() -> 1.5
add(3) 
findMedian() -> 2
'''

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        import heapq

        self.min_heap = []
        self.max_heap = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """

        if len(self.min_heap) == 0 and len(self.max_heap) == 0:
            heapq.heappush(self.min_heap, num)
            return

        if num >= self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)

        if len(self.min_heap) - len(self.max_heap) == 2:
            min_v = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_v)
            return

        if len(self.max_heap) - len(self.min_heap) == 2:
            max_v = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, max_v)
            return        

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """

        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2.0

        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return -self.max_heap[0]
        

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
