#!/usr/bin/env python
"""
Given a number of people, compute the probability of at least two people have the same birthday
"""

import math

class Solution(object):
    def computeProb(self, n):
        """
        :type n: int
        :rtype: float


        Idea: if n > 365, then definitely at least two people will has the same birthday,
        when n <= 365, we compute the probability of that these people do not have same birthday,
        1th people have 365 choice, 2nd people has 364 choice, 3rd people has 363 choice, etc.

        Using log operation to avoid float multipy overflow
        """

        assert n > 0, 'n should > 0'

        if n > 365:
            return 1.0

        prob = 0.0
        for i in xrange(n):
            prob += math.log((365 - i) / 365.0, 2)

        return 1.0 - 2.0 ** prob


class Solution2(object):
    def computeProb(self, n):
        """
        :type n: int
        :rtype: float


        Idea: if n > 365, then definitely at least two people will has the same birthday,
        when n <= 365, we compute the probability of that these people do not have same birthday,
        1th people have 365 choice, 2nd people has 364 choice, 3rd people has 363 choice, etc.

        Using log operation to avoid float multipy overflow
        """

        assert n > 0, 'n should > 0'

        if n > 365:
            return 1.0

        temp = math.log(365.0, 2)
        prob = 0.0
        for i in xrange(n):
            prob += math.log(365 - i, 2) - temp

        return 1.0 - 2.0 ** prob


class BirthdayParadoxImage(object):
    def showCurve(self):
        x = [i + 1 for i in range(365)]
        y = []

        temp = math.log(365.0, 2)

        prob = 0.0
        for n in x:
            # prob += math.log((365 - n + 1) / 365.0, 2)
            prob += math.log(365 - n + 1, 2) - temp

            current_prob = 1.0 - 2.0 ** prob
            y.append(current_prob)

        import matplotlib.pyplot as plt 
        plt.title('probability of at least two people have the same birthday')
        plt.plot(x, y, color='blue', lw=2)
        plt.show()


if __name__ == '__main__':
    so = Solution()

    print so.computeProb(20), ', at least two people have the same birthday probability of 20 people'
    print so.computeProb(23), ', at least two people have the same birthday probability of 23 people'
    print so.computeProb(30), ', at least two people have the same birthday probability of 30 people'
    print so.computeProb(40), ', at least two people have the same birthday probability of 40 people'
    print so.computeProb(364), ', at least two people have the same birthday probability of 364 people'
    print so.computeProb(365), ', at least two people have the same birthday probability of 365 people'
    print so.computeProb(400), ',  at least two people have the same birthday probability of 400 people'

    print 'show curve'
    image = BirthdayParadoxImage()
    image.showCurve()
