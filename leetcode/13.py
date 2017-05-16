'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        idx = len(s) - 1
        pre = table[s[idx]]
        num = 0
        while idx >= 0:
            cur_num = table[s[idx]]
            if cur_num < pre:
                num -= cur_num
            else:
                num += cur_num

            pre = cur_num
            idx -= 1

        return num

if __name__ == '__main__':
    so = Solution()
    
    print so.romanToInt('XCV')
    print so.romanToInt('XVI')
    print so.romanToInt('MMMCMXCIX')
         
            
        


