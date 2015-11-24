#!/usr/bin/env python
"""
Given a number of people, compute the probability of at least two people have the same birthday
"""

class Solution(object):
    def computeProb(self, n):
        """
        :type n: int
        :rtype: float


        Idea: if n > 365, then definitely at least two people will has the same birthday,
        when n <= 365, we compute the probability of that these people do not have same birthday,
        1th people have 365 choice, 2nd people has 364 choice, 3rd people has 363 choice, etc.

        Issue: precision Issue for float
        """

        assert n > 0, 'n should > 0'

        if n > 365:
            return 1.0

        prob = 1.0
        for i in xrange(n):
            prob *= (365 - i) / 365.0

        return 1.0 - prob

if __name__ == '__main__':
    so = Solution()

    print so.computeProb(20), ', probability of 20 people'
    print so.computeProb(23), ', probability of 23 people'
    print so.computeProb(40), ', probability of 40 people'
    print so.computeProb(364), ', probability of 364 people'
    print so.computeProb(365), ', probability of 365 people'
    print so.computeProb(400), ', probability of 400 people'
