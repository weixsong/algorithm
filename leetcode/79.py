# -*- encoding: utf-8 -*-
'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        if not board:
            return False
        
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, 0, i, j) == True:
                    return True

        return False

    def dfs(self, board, word, k, i, j):
        if k == len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
            return False

        temp = board[i][j]
        board[i][j] = '#'
        next = k + 1
        res = self.dfs(board, word, next, i + 1, j) or self.dfs(board, word, next, i - 1, j) or \
            self.dfs(board, word, next, i, j - 1) or self.dfs(board, word, next, i, j + 1)
        board[i][j] = temp

        return res



