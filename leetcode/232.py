'''
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
'''

class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.sin = []
        self.sout = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.sin.append(x)

    # @return nothing
    def pop(self):
        if len(self.sout) == 0:
            while len(self.sin) != 0:
                self.sout.append(self.sin.pop())

        self.sout.pop()
        

    # @return an integer
    def peek(self):
        if len(self.sout) == 0:
            while len(self.sin) != 0:
                self.sout.append(self.sin.pop())

        return self.sout[len(self.sout) - 1]
        

    # @return an boolean
    def empty(self):
        return len(self.sin) + len(self.sout) == 0

if __name__ == '__main__':

    so = Queue()

    so.push(1)
    so.push(2)
    so.push(3)
    so.pop()
    so.push(5)

    print so.peek()

