# -*- encoding: utf-8 -*-
'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cycle = set()
        while n != 1:
            if n in cycle:
                return False

            cycle.add(n)
            new_n = 0

            while n > 0:
                digit = n % 10
                new_n += digit ** 2
                n /= 10

            n = new_n

        return True

if __name__ == '__main__':
    so = Solution()

    print so.isHappy(19)
    print so.isHappy(11)
