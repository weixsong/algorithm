# -*- encoding: utf-8 -*-
'''
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

'''

class Solution(object):
    '''
    swap positive integer to its position, start from 0 put 1
    '''
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in xrange(n):
            while nums[i] > 0 and nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]

        for i in xrange(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

if __name__ == '__main__':
    so = Solution()

    print so.firstMissingPositive([2, 1])
