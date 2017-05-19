'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

Hint:

A naive implementation of the above process is trivial. Could you come up with other methods?
What are all the possible results?
How do they occur, periodically or randomly?
You may find this Wikipedia article useful.

'''

class Solution2:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        while num > 9:
            a = 0
            while num > 0:
                a += num % 10
                num = num / 10

            num = a

        return num

class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        if num <= 9:
            return num

        return (num - 10) % 9 + 1


if __name__ == '__main__':
    so = Solution()

    for i in range(100):
        print i, ':', so.addDigits(i)


