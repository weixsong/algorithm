# -*- encoding: utf-8 -*-
'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


f(n) = f(n-1) + f(n-2)
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1 or n == 2:
            return n

        n1, n2 = 1, 2
        k = 3
        ways = 0
        while k <= n:
            ways = n1 + n2
            n1 = n2
            n2 = ways
            k += 1

        return ways

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 3:
            return n

        n1, n2 = 1, 2
        ways = 0
        for k in xrange(3, n + 1):
            ways = n1 + n2
            n1, n2 = n2, ways

        return ways
        