# -*- encoding: utf-8 -*-
'''
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2^31 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Hint:

Did you see a pattern in dividing the number into chunk of words? For example, 123 and 123000.
Group the number by thousands (3 digits). You can write a helper function that takes a number less than 1000 and convert just that chunk to words.
There are many edge cases. What are some good test cases? Does your code work with input such as 0? Or 1000010? (middle chunk is zero and should not be printed out)
'''

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        base = ['', 'Thousand','Million', 'Billion']
        mmap = {1: 'One', 
                2: 'Two', 
                3: 'Three', 
                4: 'Four', 
                5: 'Five', 
                6: 'Six', 
                7: 'Seven', 
                8: 'Eight', 
                9: 'Nine', 
                10: 'Ten', 
                11: 'Eleven', 
                12: 'Twelve', 
                13: 'Thirteen', 
                14: 'Fourteen', 
                15: 'Fifteen', 
                16: 'Sixteen', 
                17: 'Seventeen', 
                18: 'Eighteen', 
                19: 'Nineteen',
                20: 'Twenty',
                30: 'Thirty',
                40: 'Forty',
                50: 'Fifty',
                60: 'Sixty',
                70: 'Seventy',
                80: 'Eighty',
                90: 'Ninety'
            }

        if num == 0:
            return 'Zero'

        base_idx = 0
        res = []
        while num > 0:
            chunk = []
            j = 0
            while j <= 2 and num > 0:
                chunk.append(num % 10)
                j += 1
                num /= 10

            temp_res = self.chunk_3(chunk, mmap)
            if base_idx != 0 and len(temp_res) != 0:
                temp_res.append(base[base_idx])
            base_idx += 1
            res = temp_res + res

        return ' '.join(res)
        
    def chunk_3(self, nums, mmap):
        base = 1
        res = []

        i = 0
        c = 0
        while i < len(nums):
            c += nums[i] * base
            if nums[i] == 0:
                i += 1
                base *= 10
                continue

            if base == 1:
                res.append(mmap[nums[i]])

            if base == 10 and nums[i] == 1:
                if len(res) != 0:
                    res.pop()
                res.append(mmap[c])

            if base == 10 and nums[i] >= 2:
                res.append(mmap[nums[i] * 10])

            if base == 100:
                res.append('Hundred')
                res.append(mmap[nums[i]])

            i += 1
            base *= 10

        res.reverse()
        return res

if __name__ == '__main__':
    so = Solution()

    print so.numberToWords(18)
    print so.numberToWords(8)
    print so.numberToWords(123)
    print so.numberToWords(214)
    print so.numberToWords(123)
    print so.numberToWords(12345)
    print so.numberToWords(1234567)
    print so.numberToWords(10)
    print so.numberToWords(1000000)




