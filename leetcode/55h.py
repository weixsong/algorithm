# -*- encoding: utf-8 -*-
'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''

class Solution1(object):
    '''
    Timeout
    '''
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        arr = [False for i in range(len(nums))]

        for i in range(len(nums) - 1):
            steps = nums[i]
            for j in range(1, steps + 1):
                if i + j < len(arr):
                    arr[i + j] = True
                    if arr[-1] == True:
                        return True

        return arr[-1]

class Solution(object):
    '''
    dynamic programming
    '''
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        m = 0
        for i in range(len(nums) - 1):
            m = max(m - 1, nums[i])
            if m == 0:
                return False

        return True

if __name__ == '__main__':

    so = Solution()

    print so.canJump([2,3,1,1,4])
    print so.canJump([3,2,1,0,4])
