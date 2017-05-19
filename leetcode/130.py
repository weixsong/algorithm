#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
"""

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board == None or len(board) == 0: return

        m, n = len(board), len(board[0])
        frontier = []
        visited = set()

        for i in range(n):
            if board[0][i] == 'O':
                frontier.append((0, i))
                visited.add((0, i))

        for j in range(1, m):
            if board[j][n - 1] == 'O':
                frontier.append((j, n - 1))
                visited.add((j, n - 1))

        for j in range(n - 1):
            if board[m - 1][j] == 'O':
                frontier.append((m - 1, j))
                visited.add((m - 1, j))

        for i in range(1, m - 1):
            if board[i][0] == 'O':
                frontier.append((i, 0))
                visited.add((i, 0))

        while len(frontier) != 0:
            top = frontier[0]
            frontier.pop(0)
            x, y = top[0], top[1]

            if x > 0 and board[x - 1][y] == 'O' and (x - 1, y) not in visited:
                frontier.append((x - 1, y))
                visited.add((x - 1, y))

            if x < m - 1 and board[x + 1][y] == 'O' and (x + 1, y) not in visited:
                frontier.append((x + 1, y))
                visited.add((x + 1, y))

            if y > 0 and board[x][y - 1] == 'O' and (x, y - 1) not in visited:
                frontier.append((x, y - 1))
                visited.add((x, y - 1))

            if y < n - 1 and board[x][y + 1] == 'O' and (x, y + 1) not in visited:
                frontier.append((x, y + 1))
                visited.add((x, y + 1))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'
        
        