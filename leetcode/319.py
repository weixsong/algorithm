#!/usr/bin/env python
'''
There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the nth round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Given n = 3. 

At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off]. 

So you should return 1, because there is only one bulb is on.
'''

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int

        O(n^2), time out
        """
        
        stat = [0] * n
        for i in range(1, n + 1):
            step = i
            i = step - 1
            while i < n:
                if stat[i] == 0:
                    stat[i] = 1
                else:
                    stat[i] = 0

                i += step

        count = 0
        for i in stat:
            if i == 1:
                count += 1

        return count

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """

        i, count = 1, 0

        while i * i <= n:
            count += 1
            i += 1

        return count







