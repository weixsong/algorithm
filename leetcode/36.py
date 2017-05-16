# -*- encoding: utf-8 -*-
'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

'''

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in s:
                    return False
                s.add(board[i][j])

        for j in range(9):
            s = set()
            for i in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in s:
                    return False

                s.add(board[i][j])

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                s = set()
                for m in range(i, i + 3):
                    for n in range(j, j + 3):
                        if board[m][n] == '.':
                            continue
                        if board[m][n] in s:
                            return False
                        s.add(board[m][n])

        return True

if __name__ == '__main__':
    so = Solution()

    print so.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])