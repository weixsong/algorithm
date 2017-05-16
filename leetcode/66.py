# -*- encoding: utf-8 -*-
'''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        carrier = 1
        i = len(digits) - 1
        while i >= 0:
            if carrier == 0:
                break

            num = digits[i] + carrier
            digits[i] = num % 10
            carrier = num / 10
            
            i -= 1
            
        if carrier != 0:
            digits.insert(0, carrier)
            
        return digits

if __name__ == '__main__':
    so = Solution()

    print so.plusOne([1,0])