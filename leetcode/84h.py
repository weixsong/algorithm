# -*- encoding: utf-8 -*-
'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.
'''

class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        height.insert(0, 0)
        height.append(0)
        n = len(height)

        stack = []
        i, res = 0, 0
        stack.append(0)

        for i in range(1, n):
            idx = stack[-1]
            while height[i] < height[idx]:
                stack.pop()
                res = max(res, height[idx] * (i - stack[-1] - 1))
                idx = stack[-1]

            stack.append(i)

        return res