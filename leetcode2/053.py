#!/usr/bin/env python


class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        acc = nums[:]
        v = nums[0]
        for i in range(1, len(nums)):
            temp = acc[i - 1] + nums[i]
            if temp < nums[i]:
                acc[i] = nums[i]
            else:
                acc[i] = temp

            if acc[i] > v:
                v = acc[i]

        return v

if __name__ == '__main__':
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    so = Solution()
    print(so.maxSubArray(arr))
