#!/usr/bin/env python
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) == 0:
            return True
        
        left, right = 0, len(s) - 1
        s = s.lower()

        while left < len(s) and right >= 0 and left < right:
            while left < len(s) and s[left].isalnum() != True:
                left += 1
            while right >= 0 and s[right].isalnum() != True:
                right -= 1

            if left >= right:
                return True
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1

        return True

if __name__ == '__main__':
    so = Solution()

    print so.isPalindrome("A man, a plan, a canal: Panama")
