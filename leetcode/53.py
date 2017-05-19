# -*- encoding: utf-8 -*-
'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
'''

class Solution(object):
    '''
    dynamic programming
    '''
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        r = nums[:]
        v = r[0]
        for i in range(1, len(nums)):
            temp = r[i - 1] + nums[i]
            if temp < nums[i]:
                r[i] = nums[i]
            else:
                r[i] = temp
                
            if r[i] > v:
                v = r[i]

        return v

if __name__ == '__main__':
    so = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print so.maxSubArray(nums)




