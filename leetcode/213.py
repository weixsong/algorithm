#!/usr/bin/env python
"""
After robbing those houses on that street, 
the thief has found himself a new place for his thievery so that he will not get too much attention. 
This time, all houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. Meanwhile, 
the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Idea: There exist two conditions, 1: we rob the first house, 2: we do not rob the first house.
        because houses are in a circle, so if we rob the first house, then we could not rob the last house,
        else if we do not rob the first house, we could rob the last house.

        Equation:
        dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]

        Time: O(n)
        Space: O(n)
        """
        
        if nums == None or len(nums) == 0:
            return 0

        if len(nums) <= 2:
            return max(nums)

        v1 = self.simple_rob(nums[:-1])
        v2 = self.simple_rob(nums[1:])
        return max(v1, v2)

    def simple_rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums == None or len(nums) == 0:
            return 0

        if len(nums) <= 2:
            return max(nums)
        
        dp = [0 for i in nums]

        dp[0], dp[1] = nums[0], nums[1]
        dp[2] = dp[0] + nums[2]

        profit = max(dp[0], dp[1], dp[2])

        for i in xrange(3, len(nums)):
            pre = dp[i - 2] if dp[i - 2] > dp [i - 3] else dp[i - 3]
            dp[i] = pre + nums[i]
            if dp[i] > profit:
                profit = dp[i]

        return profit
