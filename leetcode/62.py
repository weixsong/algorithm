# -*- encoding: utf-8 -*-
'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?
'''

class Solution(object):
    '''
    DFS, timeout, O(2^n)
    '''
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        i, j = 1, 1
        count = []
        self.dfs(i, j, m, n, count)
        return len(count)

    def dfs(self, i, j, m, n, count):
        if i == m and j == n:
            count.append(1)
            return

        if i < m:
            self.dfs(i + 1, j, m, n, count)

        if j < n:
            self.dfs(i, j + 1, m, n, count)

class Solution(object):
    '''
    dynamic programming
    f(m, n) = f(n - 1, n) + f(m, n - 1)
    '''
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        mat = [[1 for i in range(n)] for j in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                mat[i][j] = mat[i - 1][j] + mat[i][j - 1]

        return mat[-1][-1]




