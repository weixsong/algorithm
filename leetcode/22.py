# -*- encoding: utf-8 -*-
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        res = []
        stack = []
        self.DFS(n, 0, 0, stack, res)

        return res

    def DFS(self, n, left, right, stack, res):
        if left == n and right == n:
            res.append(''.join(stack[:]))

        if left < n:
            stack.append('(')
            self.DFS(n, left + 1, right, stack, res)
            stack.pop()

        if right < n and right < left:
            stack.append(')')
            self.DFS(n, left, right + 1, stack, res)
            stack.pop()



if __name__ == '__main__':

    so = Solution()
    n = 3
    print so.generateParenthesis(n)

