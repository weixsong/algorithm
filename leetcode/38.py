# -*- encoding: utf-8 -*-
'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

'''

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        if n <= 0:
            return ''

        c_str = '1'
        while n > 1:
            n_str = ''
            i = 0
            while i < len(c_str):
                j = i + 1
                count = 1
                while j < len(c_str) and c_str[j] == c_str[i]:
                    j += 1
                    count += 1

                n_str += str(count) + c_str[i]
                i = j

            n -= 1
            c_str = n_str


        return c_str

if __name__ == '__main__':
    so = Solution()

    print so.countAndSay(1)
    print so.countAndSay(2)
    print so.countAndSay(3)
    print so.countAndSay(4)
    print so.countAndSay(5)



