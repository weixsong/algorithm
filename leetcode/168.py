# -*- encoding: utf-8 -*-
'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 

'''

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        res = []
        while n > 0:
            d = n % 26
            if d == 0:
                res.append('Z')
                n /= 26
                n -= 1
            else:
                res.append(chr(d + 65 - 1))
                n /= 26

        res.reverse()
        return ''.join(res)

if __name__ == '__main__':
    so = Solution()

    print so.convertToTitle(1)
    print so.convertToTitle(26)
    print so.convertToTitle(27)
    print so.convertToTitle(28)
    print so.convertToTitle(52)
    print so.convertToTitle(53) # BA
