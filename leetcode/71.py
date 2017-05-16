# -*- encoding: utf-8 -*-
'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
'''

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        stack = []
        path = path.split('/')

        for i in range(len(path)):
            if path[i] == '' or path[i] == '.':
                continue

            elif path[i] == '..':
                if len(stack) == 0:
                    continue
                else:
                    stack.pop()
            else:
                stack.append(path[i])

        return '/' + '/'.join(stack)
            