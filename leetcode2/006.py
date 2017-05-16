#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""


class Solution(object):
    """
    Time: O(n)
    Space: O(n^2)
    """

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        mat = [[] for i in range(numRows)]
        idx = 0
        stop = False
        while idx < len(s):
            for i in range(numRows):
                mat[i].append(s[idx])
                idx += 1
                if idx >= len(s):
                    stop = True
                    break

            if stop == True:
                break

            for j in range(numRows - 2):
                target_row = numRows - 2 - j
                for k in range(numRows):
                    if k == target_row:
                        mat[k].append(s[idx])
                        idx += 1
                        if idx >= len(s):
                            stop = True
                            break
                    else:
                        mat[k].append(' ')

                if stop == True:
                    break

            if stop == True:
                break

        s = ''
        for i in range(numRows):
            for c in mat[i]:
                if c != ' ':
                    s += c

        return s


class Solution2(object):
    """
    Use the regularization
    Time: O(n)
    Space: O(n)
    """

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if len(s) <= numRows or numRows == 1:
            return s

        res = []

        # first row
        idx = 0
        gap = numRows * 2 - 2
        while idx < len(s):
            res.append(s[idx])
            idx += gap

        # middle row
        for i in range(1, numRows - 1):
            idx = i

            gap1 = numRows * 2 - 2 - i * 2
            gap2 = numRows * 2 - 2 - gap1

            while idx < len(s):
                res.append(s[idx])
                idx += gap1
                if idx < len(s):
                    res.append(s[idx])
                    idx += gap2

        # last row
        idx = numRows - 1
        while idx < len(s):
            res.append(s[idx])
            idx += gap

        return ''.join(res)


class Solution3(object):

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1 or len(s) <= numRows:
            return s

        cycle = 2 * (numRows - 1)
        res = []
        for i in xrange(numRows):
            idx = i
            step1 = cycle - 2 * i
            step2 = cycle - step1
            while idx < len(s):
                res.append(s[idx])
                if step1 == 0 or step2 == 0:
                    idx += cycle
                    continue

                idx += step1
                if idx < len(s):
                    res.append(s[idx])
                    idx += step2

        return ''.join(res)


if __name__ == '__main__':
    so = Solution3()
    print(so.convert('PAYPALISHIRING', 3))
    print(so.convert('ABCDE', 4))
    print(so.convert('A', 1))
