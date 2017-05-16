# -*- encoding: utf-8
'''
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
'''

class Solution2(object):
    '''
    timeout
    '''
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        neg = False
        if dividend < 0 and divisor > 0:
            neg = True
        elif dividend > 0 and divisor < 0:
            neg = True

        res = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            dividend -= divisor
            res += 1

        if neg == True: return -res
        return res

class Solution(object):
    '''
    by bit operation
    << >>  and so on
    '''
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        MAX_INT = 2147483647
        if divisor == 0:
            return MAX_INT
        
        neg = False
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            neg = True

        a, b = abs(dividend), abs(divisor)
        dvs = b
        step = 0
        while dvs <= a:
            dvs = dvs << 1
            step += 1

        res = 0
        while a >= b:
            if a >= dvs:
                a -= dvs
                res = res + (1 << step)

            dvs = dvs >> 1
            step -= 1

        if neg == True:
            res = -res
        if res > MAX_INT:
            return MAX_INT
        if res < -(MAX_INT + 1):
            return -(MAX_INT + 1)

        return res

if __name__ == '__main__':
    so = Solution()

    print so.divide(-2147483648, 1)










