#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up: 
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""

class Solution1(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        m, n = len(board), len(board[0])
        mat = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                mat[i][j] = self.get_state(board, i, j, m, n)

        for i in range(m):
            for j in range(n):
                board[i][j] = mat[i][j]


    def get_state(self, board, i, j, m, n):
        neighbors = []
        if i - 1 >= 0:
            neighbors.append(board[i - 1][j])

        if i + 1 < m:
            neighbors.append(board[i + 1][j])

        if j - 1 >= 0:
            neighbors.append(board[i][j - 1])

        if j + 1 < n:
            neighbors.append(board[i][j + 1])

        if i - 1 >= 0 and j - 1 >= 0:
            neighbors.append(board[i - 1][j - 1])

        if i - 1 >= 0 and j + 1 < n:
            neighbors.append(board[i - 1][j + 1])

        if i + 1 < m and j - 1 >= 0:
            neighbors.append(board[i + 1][j - 1])

        if i + 1 < m and j + 1 < n:
            neighbors.append(board[i + 1][j + 1])

        one_sum = neighbors.count(1)
        zero_sum = neighbors.count(0)
        cur_state = board[i][j]
        if cur_state == 1:
            if one_sum < 2: return 0
            if one_sum == 2 or one_sum == 3: return 1
            if one_sum > 3: return 0
        if cur_state == 0:
            if one_sum == 3: return 1

        return 0

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                self.get_state(board, i, j, m, n)

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1


    def get_state(self, board, i, j, m, n):
        neighbors = []
        if i - 1 >= 0:
            neighbors.append(board[i - 1][j])

        if i + 1 < m:
            neighbors.append(board[i + 1][j])

        if j - 1 >= 0:
            neighbors.append(board[i][j - 1])

        if j + 1 < n:
            neighbors.append(board[i][j + 1])

        if i - 1 >= 0 and j - 1 >= 0:
            neighbors.append(board[i - 1][j - 1])

        if i - 1 >= 0 and j + 1 < n:
            neighbors.append(board[i - 1][j + 1])

        if i + 1 < m and j - 1 >= 0:
            neighbors.append(board[i + 1][j - 1])

        if i + 1 < m and j + 1 < n:
            neighbors.append(board[i + 1][j + 1])

        one_sum = 0
        for n in neighbors:
            one_sum += n & 1

        cur_state = board[i][j] & 1
        if cur_state == 1 and (one_sum == 2 or one_sum == 3):
            board[i][j] |= 2

        if cur_state == 0 and (one_sum == 3):
            board[i][j] |= 2
