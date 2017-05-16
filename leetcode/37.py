# -*- encoding: utf-8 -*-
'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.


A sudoku puzzle...


...and its solution numbers marked in red.

'''

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """


        if board == None or len(board) == 0 and len(board[0]) == 0:
            return

        cand = '123456789'
        self.solve(board, cand)

    def solve(self, board, cand):
        '''
        DFS
        '''

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    continue

                for c in cand:
                    if self.check(board, i, j, c) == True:
                        board[i][j] = c

                        res = self.solve(board, cand)

                        if res == True:
                            return True

                        board[i][j] = '.'

                return False

        return True


    def check(self, board, i, j, c):
        for row in range(9):
            if board[row][j] == c:
                return False

        for col in range(9):
            if board[i][col] == c:
                return False
        

        row = i / 3 * 3
        col = j / 3 * 3

        for m in range(row, row + 3):
            for n in range(col, col + 3):
                if board[m][n] == c:
                    return False

        return True

