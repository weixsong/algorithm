# -*- encoding: utf-8 -*-
'''
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

'''

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        mat = [[0 for i in range(n)] for j in range(n)]

        seq = 0
        for row in xrange(n / 2):
            for i in xrange(row, n - 1 - row):
                seq += 1
                mat[row][i] = seq

            for i in xrange(row, n - 1 - row):
                seq += 1
                mat[i][n - 1 - row] = seq

            for i in xrange(n - 1 - row, row, -1):
                seq += 1
                mat[n - 1 - row][i] = seq

            for i in xrange(n - 1 - row, row, -1):
                seq += 1
                mat[i][row] = seq

        if n % 2 == 1:
            mat[n / 2][n / 2] = seq + 1

        return mat

if __name__ == '__main__':
    so = Solution()

    print so.generateMatrix(3)
    print so.generateMatrix(4)