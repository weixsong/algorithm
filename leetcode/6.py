#!/usr/bin/env python

"""
ZigZag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s

        cycle = 2 * (numRows - 1)
        res = []
        for i in xrange(numRows):
            if i >= len(s):
                break

            idx = i
            res.append(s[idx])
            while idx < len(s):
                step = cycle - 2 * i
                if idx + step >= len(s):
                    break

                if step != 0:
                    idx += step
                    res.append(s[idx])

                step2 = cycle - step
                if step2 == 0:
                    continue

                if step2 + idx >= len(s):
                    break

                idx += step2
                res.append((s[idx]))

        return ''.join(res)


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s

        cycle = 2 * (numRows - 1)
        res = []
        for i in xrange(numRows):
            if i >= len(s):
                break

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
    so = Solution()
    s = 'PAYPALISHIRING'

    print so.convert(s, 3)
