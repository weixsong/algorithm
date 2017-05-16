'''
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        digit = 1
        romar = []
        while num > 0:
            remainder = num % 10
            num = num / 10

            res = ''
            if digit == 1:
                if remainder == 9:
                    romar.append('IX')
                elif remainder >= 5:
                    romar.append('V' + 'I'*(remainder-5))
                elif remainder > 3:
                    romar.append('IV')
                else:
                    romar.append('I' * remainder)

            elif digit == 2:
                if remainder == 9:
                    romar.append('XC')
                elif remainder >= 5:
                    romar.append('L' + 'X'*(remainder-5))
                elif remainder > 3:
                    romar.append('XL')
                else:
                    romar.append('X' * remainder)

            elif digit == 3:
                if remainder == 9:
                    romar.append('CM')
                elif remainder >= 5:
                    romar.append('D' + 'C'*(remainder-5))
                elif remainder > 3:
                    romar.append('CD')
                else:
                    romar.append('C' * remainder)

            elif digit == 4:
                romar.append('M' * remainder)

            digit += 1

        romar.reverse()
        return ''.join(romar)

if __name__ == '__main__':
    so = Solution()
    
    print so.intToRoman(7)
    print so.intToRoman(999)
    print so.intToRoman(3999)
