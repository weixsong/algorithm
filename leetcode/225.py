'''
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
'''

class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.q1 = []
        self.q2 = []
        self.head = None

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.head = x
        if len(self.q1) != 0:
            self.q1.append(x)
        else:
            self.q2.append(x)        

    # @return nothing
    def pop(self):
        if len(self.q1) == 0:
            while len(self.q2) > 1:
                self.head = self.q2.pop(0)
                self.q1.append(self.head)
            self.q2.pop()
        else:
            while len(self.q1) > 1:
                self.head = self.q1.pop(0)
                self.q2.append(self.head)
            self.q1.pop()

    # @return an integer
    def top(self):
        return self.head

    # @return an boolean
    def empty(self):
        return len(self.q1) + len(self.q2) == 0

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.pop()
    print s.top()
