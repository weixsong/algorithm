# -*- encoding: utf-8 -*-
'''
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
'''

class Solution1(object):
    '''
    Memory out for large number
    '''
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        if num == 1:
            return True

        is_prime = [True for i in range(num + 1)]
        is_prime[0] = False
        is_prime[1] = False

        for i in range(2, num + 1):
            if is_prime[i] == True:
                if i not in [2, 3, 5]:
                    return False

                j = i * 2
                while j <= num:
                    is_prime[j] = False
                    j += i

        return True

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False

        while num >= 2:
            if num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
                return False

            if num % 2 == 0:
                num /= 2
            elif num % 3 == 0:
                num /= 3
            elif num % 5 == 0:
                num /= 5

        return True
        
if __name__ == '__main__':

    so = Solution()

    print so.isUgly(2)
    print so.isUgly(14)




