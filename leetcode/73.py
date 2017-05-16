# -*- encoding: utf-8 -*-
'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        m, n = len(matrix), len(matrix[0])
        rows, cols = [], []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)

        for row in rows:
            for j in range(n):
                matrix[row][j] = 0

        for col in cols:
            for i in range(m):
                matrix[i][col] = 0

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(n):
                        if matrix[i][k] != 0:
                            matrix[i][k] = None
                    for k in range(m):
                        if matrix[k][j] != 0:
                            matrix[k][j] = None

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == None:
                    matrix[i][j] = 0
