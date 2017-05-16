# -*- encoding: utf-8 -*-
'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
'''

class Solution1(object):
    '''
    matrix multiply
    O(n^3)
    '''
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        #for row in matrix:
        #    for item in row:
        #        print item,
        #    print

        rotate = [[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            rotate[i][n - 1 - i] = 1

        # print rotate
        #for row in rotate:
        #    for item in row:
        #        print item,
        #    print

        # mutiply
        for i in range(n):
            t = [0 for dummpy_i in range(n)]
            for j in range(n):
                for k in range(n):
                    t[j] += matrix[i][k] * rotate[k][j]

            for j in range(n):
                matrix[i][j] = t[j]

class Solution(object):
    '''
    move directly
    O(n^2)
    '''
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        for row in range(n / 2):
            for col in range(row, n - row - 1):
                temp = matrix[row][col]
                matrix[row][col] = matrix[n - 1 - col][row]
                matrix[n - 1 - col][row] = matrix[n - 1 - row][n - 1 - col]
                matrix[n - 1 - row][n - 1 - col] = matrix[col][n - 1 - row]
                matrix[col][n - 1 - row] = temp


if __name__ == '__main__':
    so = Solution()

    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    so.rotate(matrix)

    for row in matrix:
        for i in row:
            print i,
        print



