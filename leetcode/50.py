#!/usr/bin/env python
"""
Implement pow(x, n).
"""

class Solution(object):
    def pow(self, x, n):
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
            x *= x

        return res

if __name__ == '__main__':
    so = Solution()

    print so.pow(0, 0), ', 0'
    print so.pow(2, 5), ', 32'
    print so.pow(4, 4), ', 256'
    print so.pow(3.5, 6), ', 1838.265625'
    print so.pow(1, 99999999999), ', 1'
    print so.pow(5, 8), ', 390625'
