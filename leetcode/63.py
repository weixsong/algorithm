# -*- encoding: utf-8 -*-
'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
'''

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        mat = [[1 for i in range(n)] for j in range(m)]

        for i in range(m):
            if obstacleGrid[i][0] == 1:
                while i < m:
                    mat[i][0] = 0
                    i += 1

                break

        for j in range(n):
            if obstacleGrid[0][j] == 1:
                while j < n:
                    mat[0][j] = 0
                    j += 1

                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    mat[i][j] = 0
                    continue

                mat[i][j] = mat[i - 1][j] + mat[i][j - 1]

        return mat[-1][-1]


