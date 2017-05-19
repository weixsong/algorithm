# -*- encoding: utf-8 -*-
'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        i, j = len(a) - 1, len(b) - 1
        carrier = 0

        res = []
        while i >= 0 and j >= 0:
            temp = int(a[i]) + int(b[j]) + carrier
            carrier = temp / 2
            dvd = temp % 2
            res.append(str(dvd))

            i -= 1
            j -= 1

        while i >= 0:
            temp = int(a[i]) + carrier
            carrier = temp / 2
            dvd = temp % 2
            res.append(str(dvd))

            i -= 1

        while j >= 0:
            temp = int(b[j]) + carrier
            carrier = temp / 2
            dvd = temp % 2
            res.append(str(dvd))

            j -= 1

        if carrier != 0:
            res.append(str(carrier))

        res.reverse()

        return ''.join(res)
