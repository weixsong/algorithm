# -*- encoding: utf-8 -*-
'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        for ch in s:
            if ch in '([{':
                if ch == '(':
                    stack.append(')')
                if ch == '[':
                    stack.append(']')
                if ch == '{':
                    stack.append('}')
                continue

            elif ch in ')]}':
                if len(stack) == 0:
                    return False

                top = stack[len(stack) - 1]
                if top != ch:
                    return False
                else:
                    stack.pop()
                    
        return len(stack) == 0

if __name__ == '__main__':
    so = Solution()

    print so.isValid('()[]{}')
