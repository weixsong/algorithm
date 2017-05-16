# -*- encoding: utf-8 -*-
'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return 0

        mid, idx = 0, 0
        for i in xrange(len(height)):
            if height[i] > mid:
                mid = height[i]
                idx = i

        count = 0

        left, right = 0, len(height) - 1
        maxh = height[left]
        while left < idx:
            if height[left] > maxh:
                maxh = height[left]
            else:
                count += maxh - height[left]

            left += 1

        maxh = height[right]
        while right > idx:
            if height[right] > maxh:
                maxh = height[right]
            else:
                count += maxh - height[right]

            right -= 1

        return count

if __name__ == '__main__':
    so = Solution()

    print so.trap([0,1,0,2,1,0,1,3,2,1,2,1])



