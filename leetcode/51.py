# -*- encoding: utf-8 -*-
'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

'''

class Solution2(object):
    '''
    timeout
    even for only n = 6, need to compute for a while
    '''
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        board = [['.' for j in range(n)] for i in range(n)]
        res = set()
        self.solve(board, res, n)

        return list(res)

    def solve(self, board, res, n):
        if n == 0:
            res.add(self.copy_board(board))
            return

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 'Q':
                    continue

                if self.check(board, i, j) == True:
                    board[i][j] = 'Q'

                    self.solve(board, res, n - 1)

                    board[i][j] = '.'


    def check(self, board, row, col):
        for i in range(len(board)):
            if board[i][col] == 'Q':
                return False

        for j in range(len(board)):
            if board[row][j] == 'Q':
                return False

        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        i, j = row, col
        while i < len(board) and j < len(board):
            if board[i][j] == 'Q':
                return False
            i += 1
            j += 1

        i, j = row, col
        while i >= 0 and j < len(board):
            if board[i][j] == 'Q':
                return False

            i -= 1
            j += 1

        i, j = row, col
        while i < len(board) and j >= 0:
            if board[i][j] == 'Q':
                return False

            i += 1
            j -= 1

        return True

    def copy_board(self, board):
        new_board = [''.join(row) for row in board]
        return tuple(new_board)

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        board = [['.' for j in range(n)] for i in range(n)]
        col_set = set()
        res = []
        self.solve(board, 0, col_set, res, n)

        return res

    def solve(self, board, row, col_set, res, n):
        if n == 0:
            res.append(self.copy_board(board))
            return

        for col in range(len(board)):
            if col in col_set:
                continue

            if self.check(board, row, col) == False:
                continue

            col_set.add(col)

            board[row][col] = 'Q'
            self.solve(board, row + 1, col_set, res, n - 1)

            board[row][col] = '.'
            col_set.remove(col)

    def copy_board(self, board):
        return [''.join(row) for row in board]

    def check(self, board, row, col):
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        i, j = row, col
        while i >= 0 and j < len(board):
            if board[i][j] == 'Q':
                return False

            i -= 1
            j += 1

        return True
        

if __name__ == '__main__':
    so = Solution()

    print so.solveNQueens(4)
    print so.solveNQueens(6)
