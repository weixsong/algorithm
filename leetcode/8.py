"""
String to Integer
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        max_int = 2147483647
        min_int = -2147483648

        if len(str) == 0:
            return 0

        str = str.strip()

        negative = False
        idx = 0
        if str[0] == '-':
            negative = True
            idx += 1
        elif str[0] == '+':
            idx += 1

        number = 0
        for i in xrange(idx, len(str)):
            c = str[i]
            d = ord(c) - 48
            if d < 0 or d > 9:
                break

            number = number * 10 + d

        if negative is True:
            number = -number

        if number > max_int:
            number = max_int
        if number < min_int:
            number = min_int

        return number
