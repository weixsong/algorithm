#!/usr/bin/env python

"""
Given an integer, write a function to determine if it is a power of two.
"""

class Power(object):
    """
    Power contains some static function that could do quick bit operation.
    """

    def isPowerOfTwo(self, n):
        """
        Is n a power of 2.

        :type n: int
        :rtype: bool

        Given an integer, write a function to determine if it is a power of two.

        Idea: bit operation, if n is power of 2, then it bit representation only contains one 1, 
        then n & (n - 1) would be 0, otherwise n & (n - 1) != 0

        Time: O(1)
        Space: O(1)
        """

        if n == 0:
            return False

        return n & (n - 1) == 0

if __name__ == '__main__':
    so = Power()

    print so.isPowerOfTwo(0), ', Target: False,  O is not power of 2'
    print so.isPowerOfTwo(1), ', Target: True, 1 is power of 2'
    print so.isPowerOfTwo(2), ', Target: True, 2 is power of 2'
    print so.isPowerOfTwo(10), ', Target: False, 10 is not power of 2'
    print so.isPowerOfTwo(128), ', Target: True, 128 is power of 2'
    print so.isPowerOfTwo(-2), ', Target: False, -2 is not power of 2'
