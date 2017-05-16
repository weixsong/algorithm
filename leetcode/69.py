# -*- encoding: utf-8 -*-
'''
Implement int sqrt(int x).

Compute and return the square root of x.
'''

class Solution(object):
    '''
    binary search
    '''
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        left, right = 0, x
        while left <= right:
            mid = left + (right - left) / 2
            sqrt = mid * mid
            if sqrt == x:
                return mid
            elif sqrt < x:
                left = mid + 1
            else:
                right = mid - 1
                
        return left - 1
        
if __name__ == '__main__':
    so = Solution()

    print so.mySqrt(26)
    print so.mySqrt(24)
    print so.mySqrt(16)