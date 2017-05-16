# -*- encoding: utf-8 -*-
'''
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
'''

class Solution2(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        res = []

        idx = 0
        for i in xrange(len(num1) - 1, -1, -1):
            idx = len(num1) - 1 - i
            carrier = 0
            for j in xrange(len(num2) - 1, -1, -1):
                m = int(num1[i]) * int(num2[j]) + carrier

                pos = idx + len(num2) - 1 - j
                if pos < len(res):
                    v = res[pos] + m
                    res[pos] = v % 10
                    carrier = v / 10
                else:
                    res.append(m % 10)
                    carrier = m / 10

            if carrier != 0:
                pos = idx + len(num2)
                if pos < len(res):
                    v = res[pos] + carrier
                    res[pos] = v % 10
                    carrier = v / 10
                else:
                    res.append(carrier)
                    carrier = 0

        while len(res) > 0 and res[len(res) - 1] == 0:
            res.pop()

        if len(res) == 0: return '0'
        res.reverse()
        return ''.join([str(num) for num in res])

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        n1 = int(num1)
        n2 = int(num2)

        res = n1 * n2

        res = str(res)
        return res

if __name__ == '__main__':
    so = Solution()

    print so.multiply('111', '333')
    print so.multiply('111', '222')
    print so.multiply('222', '333')
    print so.multiply('222', '0')

    print so.multiply('100', '9133')

