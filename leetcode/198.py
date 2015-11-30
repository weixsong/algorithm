#!/usr/bin/env python
"""
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses 
have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Idea: dynamic programming
        could rob house by interval 1 or interval 2, there is no need to rob by interval 3,
        because you want rob more money, interval 3 will definitely lose some mony.

        dynamic programming equation:
        dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]

        Time: O(n)
        Space: O(n)
        """

        if nums == None or len(nums) == 0:
            return 0

        if len(nums) <= 2:
            return max(nums)
        
        dp = [0 for i in nums]

        dp[0], dp[1] = nums[0], nums[1]
        dp[2] = dp[0] + nums[2]

        for i in xrange(3, len(nums)):
            dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]

        return dp[-1] if dp[-1] > dp[-2] else dp[-2]
