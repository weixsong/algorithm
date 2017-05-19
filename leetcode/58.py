# -*- encoding: utf-8 -*-
'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.

'''

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        length = 0
        i = len(s) - 1

        while i >= 0 and s[i] == ' ':
            i -= 1

        j = i
        while j >= 0 and s[j] != ' ':
            j -= 1

        return i - j


if __name__ == '__main__':
    so = Solution()

    print so.lengthOfLastWord('Hello World')
