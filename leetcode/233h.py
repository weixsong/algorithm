# -*- encoding: utf-8 -*-
'''
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
'''

class Solution2(object):
    '''
    time out
    '''
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """

        i = 1
        count = 0
        while i <= n:
            k = i
            while k > 0:
                if k % 10 == 1:
                    count += 1

                k = k / 10

            i += 1

        return count

class Solution(object):
    '''
    if n % 10 == 1: 那么当前计算的所有的数都可以加上1， 这样就增加了current_total个数字
    将当前数字按照base * 10分成k份，这样就可以计算每一份中出现1的个数以及所有的k份中出现的1的个数
    '''
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """

        count = 0
        base, current_total = 1, 1

        while n > 0:
            count += (n + 8) / 10 * base + (n % 10 == 1) * current_total
            current_total += (n % 10) * base
            base *= 10
            n /= 10

        return count


if __name__ == '__main__':
    so2 = Solution2()

    print so2.countDigitOne(20)

    so = Solution()
    print so.countDigitOne(20)
