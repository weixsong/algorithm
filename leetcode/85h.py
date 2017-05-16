# -*- encoding: utf-8 -*-
'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
'''

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if not matrix:
            return 0

        row, col = len(matrix), len(matrix[0])
        m = [[0] * col for _ in range(row)]

        for j in range(col):
            if matrix[0][j] == '1':
                m[0][j] = 1

        for i in range(1, row):
            for j in range(col):
                if matrix[i][j] == '1':
                    m[i][j] = m[i - 1][j] + 1

        return max(self.largestRectangleArea(row) for row in m)
        

    def largestRectangleArea(self, height):
        height.insert(0, 0)
        height.append(0)
        n = len(height)

        stack = []
        i, res = 0, 0
        stack.append(0)

        for i in range(1, n):
            idx = stack[-1]
            while height[i] < height[idx]:
                stack.pop()
                res = max(res, height[idx] * (i - stack[-1] - 1))
                idx = stack[-1]

            stack.append(i)

        return res
