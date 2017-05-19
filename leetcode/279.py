# -*- encoding: utf-8 -*-
'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

'''

class Solution(object):
    '''
    dynamic programming
    timeout, :(
    '''
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n <= 3:
            return n

        dp = [0 for i in range(n + 1)]
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3

        for i in range(4, n + 1):
            j = 1
            v = dp[i - 1] + 1
            while j * j <= i:
                if dp[i - j * j] + 1 < v:
                    v = dp[i - j * j] + 1
                j += 1

            dp[i] = v

        return dp[-1]

class Solution(object):
    '''
    use some number theory 
    I don't think this is good exercise, not everyone need to know the number theory
    O(n)
    '''
    def numSquares(self, n):
        d1, d2 = set(), set()
        i = 1
        while i * i <= n:
            d1.add(i * i)
            i += 1

        if n in d1: return 1

        for p in d1:
            for q in d1:
                d2.add(p + q)

        if n in d2: return 2

        for p in d1:
            if n - p in d2:
                return 3

        return 4

if __name__ == '__main__':
    so = Solution()

    print so.numSquares(7)
    print so.numSquares(9)
    print so.numSquares(12)