#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
 Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        p1, p2 = 0, 0
        longest = 0

        table = {}
        while p1 < len(s) and p2 < len(s):
            while p2 < len(s) and s[p2] not in table:
                table[s[p2]] = 1
                p2 += 1

            length = p2 - p1
            if length > longest:
                longest = length

            if p2 == len(s):
                return longest

            while p1 < p2 and s[p1] != s[p2]:
                table.pop(s[p1])
                p1 += 1

            table.pop(s[p1])
            p1 += 1

        return longest


if __name__ == '__main__':
    so = Solution()
    print(so.lengthOfLongestSubstring("abcabcbb"))
    print(so.lengthOfLongestSubstring("bbbbb"))
    print(so.lengthOfLongestSubstring("pwwkew"))
