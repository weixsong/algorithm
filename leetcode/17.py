'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
'''

class Solution:
    table = {'1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        if digits == None or len(digits) == 0:
            return []

        res = ['']
        for digit in digits:
            temp = []
            for comb in res:
                for c in Solution.table[digit]:
                    temp.append(comb + c)

            res = temp[:]

        return res


if __name__ == '__main__':
    so = Solution()

    print so.letterCombinations('23')

