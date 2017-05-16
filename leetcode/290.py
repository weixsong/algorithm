#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        j = 0
        words = str.split()

        if len(words) != len(pattern):
            return False

        table1 = {}
        table2 = {}

        j = 0
        for p in pattern:
            word = words[j]
            if p in table1 or word in table2:
                j += 1
                continue

            table1[p] = word
            table2[word] = p
            j += 1

        j = 0
        for p in pattern:
            if p not in table1:
                return False

            if table1[p] != words[j]:
                return False

            j += 1

        return True

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        words = str.split()

        if len(words) != len(pattern):
            return False

        table = {}
        for i in range(len(pattern)):
            c = pattern[i]
            word = words[i]

            if c in table and table[c] != word:
                return False
            if c not in table and word in table.values():
                return False

            table[c] = word

        return True

if __name__ == '__main__':
    so = Solution()
    print so.wordPattern('abba', "dog cat cat dog")
    print so.wordPattern('abbd', "dog dog dog dog")
    print so.wordPattern('deadbeef', "d e a d b e e f")
