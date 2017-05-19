# -*- encoding: utf-8 -*-
'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
'''

class Solution2(object):
    '''
    dynamic programming
    O(n^2)
    timeout
    '''
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dp = [0 for i in range(len(nums))]

        for i in range(1, len(nums)):
            res = []
            for j in range(i):
                if nums[j] >= i - j:
                    res.append(dp[j] + 1)

            dp[i] = min(res)

        return dp[-1]

class Solution(object):
    '''
    greedy algorithm
    '''
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n, step = len(nums), 0
        start, end = 0, 0

        while end < n - 1:
            step += 1

            maxend = end + 1
            for i in range(start, end + 1):
                if nums[i] + i >= n - 1:
                    return step
                maxend = max(maxend, nums[i] + i)

            start, end = end + 1, maxend

        return step




if __name__ == '__main__':
    so = Solution()

    print so.jump([2,3,1,1,4])
