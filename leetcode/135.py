#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
"""

class Solution2(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int

        O(n^2), timeout
        """
        
        if ratings == None or len(ratings) == 0:
            return 0

        n = len(ratings)
        dp = [1] * len(ratings)

        pre = ratings[0]

        for i in range(1, n):
            rate = ratings[i]
            if rate > pre:
                dp[i] = dp[i - 1] + 1
                pre = rate
            else:
                dp[i] = 1
                j = i - 1
                while j >= 0 and ratings[j] > ratings[j + 1] and dp[j] <= dp[j + 1]:
                    dp[j] += 1
                    j -= 1

        return sum(dp)

class Solution1(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if ratings == None or len(ratings) == 0:
            return 0

        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(n - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                candies[i - 1] = max(candies[i] + 1, candies[i - 1])

        return sum(candies)

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        
        if ratings == None or len(ratings) == 0:
            return 0

        if len(ratings) < 2:
            return 1

        n = len(ratings)
        pre, total, desc = 1, 1, 0

        for i in range(1, n):
            if ratings[i] >= ratings[i - 1]:
                if desc > 0:
                    total += (1 + desc) * desc / 2
                    if desc >= pre:
                        total += desc - pre + 1
                    desc = 0
                    pre = 1
                if ratings[i] == ratings[i - 1]:
                    pre = 1
                else:
                    pre += 1

                total += pre
            else:
                desc += 1

        if desc > 0:
            total += (1 + desc) * desc / 2
            if desc >= pre:
                total += desc - pre + 1

        return total
        
if __name__ == '__main__':
    so = Solution()
    print so.candy([0])
    print so.candy([2, 2])
    print so.candy([1,2,2])