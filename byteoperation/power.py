#!/usr/bin/env python

class Power(object):
    """
    Power contains some static function that could do quick bit operation.
    """

    @staticmethod
    def isPowerOfTwo(n):
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

    @staticmethod
    def pow(x, n):
        """
        Implement pow(x, n).

        :type x: float
        :type n: int
        :rtype: float

        Idea: n = b7b6b5b4b3b2b1b0 (bit representation of n)
        n = b7 * 2^7 + b6 * 2^6 + b5 * 2^5 + b4 * 2^4 + b3 * 2^3 + b2 * 2^2 + b1 * 2^1 + b0 * 2^0
        x^n = x ^ (b7 * 2^7 + b6 * 2^6 + b5 * 2^5 + b4 * 2^4 + b3 * 2^3 + b2 * 2^2 + b1 * 2^1 + b0 * 2^0)
            = x^(b7*2^7)*x^(b6*2^6)*x^(b5*2^5)*......*x^(b0*2^0)

        In each iteration, check if ith bit is 1, if is 1, then multipy corresponding weight: x^(b5*2^5)
        Key idea is that use bit movement to do quickly pow

        Time: O(1) <= O(64) <= O(bits(n))
        Space: O(1)
        """

        if x == 0:
            return 0.0
        if n == 0 or x == 1:
            return 1.0

        if n < 0:
            x, n = 1.0/x, -n

        idx = 1
        res = 1.0
        while idx <= n:
            if idx & n != 0:
                res *= x

            idx <<= 1

        return res
