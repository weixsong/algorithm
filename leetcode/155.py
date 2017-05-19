# -*- encoding: utf-8 -*-
'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """

        self.stack = []
        self.min_stack = []
        self.size = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """

        c_min = None
        if self.size == 0:
            c_min = x
        else:
            pre_min = self.min_stack[self.size - 1]
            if x < pre_min:
                c_min = x
            else:
                c_min = pre_min

        self.min_stack.append(c_min)
        self.stack.append(x)
        self.size += 1
        

    def pop(self):
        """
        :rtype: nothing
        """

        if self.size > 0:
            self.stack.pop()
            self.min_stack.pop()
            self.size -= 1
        

    def top(self):
        """
        :rtype: int
        """

        if self.size == 0:
            return None

        return self.stack[self.size - 1]
        

    def getMin(self):
        """
        :rtype: int
        """

        if self.size == 0:
            return None

        return self.min_stack[self.size - 1]
