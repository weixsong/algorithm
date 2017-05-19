# -*- encoding: utf-8 -*-
'''
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?
'''

class Solution2(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """

        reverse = 0
        k = 32
        while k > 0:
            reverse = reverse * 2 + n % 2
            n /= 2
            k -= 1

        return reverse

class Solution1(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """

        reverse = 0
        k = 0x80000000
        while k > 0:
            reverse = (reverse << 1) + n % 2
            n = n >> 1
            k = k >> 1

        return reverse

class Solution(object):
    def __init__(self):
        k = 0x80000000
        self.dict = {}
        base = 1
        while k > 0:
            self.dict[k] = base
            base *= 2
            k = k >> 1

        self.dict[0] = 0

    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """

        reverse = 0
        k = 0x80000000
        while k > 0:
            reverse += self.dict[n & k]
            k = k >> 1

        return reverse

if __name__ == '__main__':
    so = Solution()

    n = 43261596

    print so.reverseBits(n)

