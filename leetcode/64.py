# -*- encoding: utf-8 -*-
'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m, n = len(grid), len(grid[0])

        mat = [[0 for j in range(n)] for i in range(m)]
        mat[0][0] = grid[0][0]

        for i in range(1, m):
            mat[i][0] = mat[i - 1][0] + grid[i][0]

        for j in range(1, n):
            mat[0][j] = mat[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                mat[i][j] = min(mat[i - 1][j], mat[i][j - 1]) + grid[i][j]

        return mat[-1][-1]
