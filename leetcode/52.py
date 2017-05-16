# -*- encoding: utf-8 -*-
'''
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.

'''

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        board = [['.' for j in range(n)] for i in range(n)]
        col_set = set()
        res = []
        self.solve(board, 0, col_set, res, n)

        return len(res)

    def solve(self, board, row, col_set, res, n):
        if n == 0:
            res.append(1)
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

class Solution2(object):
    '''
    Actually this algorithm will lead to timeout
    '''
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count = 0
        col_index = [i for i in range(n)]
        self.permutation(col_index, 0)

        return self.count

    def permutation(self, nums, k):
        if k == len(nums):
            if self.check(nums) == True:
                self.count += 1
            return

        for i in range(k, len(nums)):
            nums[k], nums[i] = nums[i], nums[k]
            self.permutation(nums, k + 1)
            nums[k], nums[i] = nums[i], nums[k]

    def check(self, nums):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and abs(i - j) == abs(nums[i] - nums[j]):
                    return False

        return True

if __name__ == '__main__':
    so = Solution()

    print so.totalNQueens(4)
    print so.totalNQueens(6)
    print so.totalNQueens(9)





