# -*- encoding: utf-8 -*-
'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
'''


class Solution1(object):
    '''
    dynamic programming directly
    O(n)
    '''
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        dp = [0 for i in range(len(s))]

        max_v = 0

        for i in xrange(len(s) - 2, -1, -1):
            if s[i] != '(':
                continue

            j = i + 1 + dp[i + 1]
            if j < len(s) and ')' == s[j]:
                dp[i] = dp[i + 1] + 2
                if j + 1 < len(s):
                    dp[i] += dp[j + 1]

                if dp[i] > max_v:
                    max_v = dp[i]

        return max_v

class Solution(object):
    '''
    采用一个数组对匹配的括号进行标记，然后查找最长的连续匹配标记
    O(n)
    '''
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        flag = [False for i in range(len(s))]

        stack = []
        for i in xrange(len(s)):
            if s[i] == '(':
                stack.append(i)
                continue

            if len(stack) == 0:
                continue

            flag[i] = True
            flag[stack[len(stack) - 1]] = True
            stack.pop()

        max_v = 0
        cur_v = 0
        for key in flag:
            if key == True:
                cur_v += 1

            else:
                if cur_v > max_v:
                    max_v = cur_v

                cur_v = 0

        if cur_v > max_v:
            max_v = cur_v

        return max_v



if __name__ == '__main__':
    so = Solution()

    print so.longestValidParentheses("(()")
    print so.longestValidParentheses(")()())")
    print so.longestValidParentheses("()(()")
    print so.longestValidParentheses("(())()")




