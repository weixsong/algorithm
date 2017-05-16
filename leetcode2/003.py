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
    """
    Use hashset to record what char is covered
    Time: O(n)
    Space: O(n)
    """
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


class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        p1, p2 = 0, 0
        longest = 0

        collection = set()
        while p1 < len(s) and p2 < len(s):
            while p2 < len(s) and s[p2] not in collection:
                collection.add(s[p2])
                p2 += 1

            length = p2 - p1
            if length > longest:
                longest = length

            if p2 == len(s):
                return longest

            while p1 < p2 and s[p1] != s[p2]:
                collection.remove(s[p1])
                p1 += 1

            collection.remove(s[p1])
            p1 += 1

        return longest


class Solution3(object):
    """
    This one is the best
    Time: O(n)
    Space: O(n)
    """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        p1, p2, longest = 0, 0, 0

        collection = set()
        while p2 < len(s):
            c = s[p2]
            if c not in collection:
                collection.add(c)
                p2 += 1
            else:
                d = p2 - p1
                if d > longest:
                    longest = d

                while c in collection:
                    collection.remove(s[p1])
                    p1 += 1

        if p2 - p1 > longest:
            longest = p2 - p1

        return longest


class Solution4(object):
    """
    This one is the best
    Time: O(n)
    Space: O(n)
    """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        p1, p2, longest = 0, 0, 0

        collection = set()
        while p2 < len(s):
            c = s[p2]
            if c not in collection:
                collection.add(c)
                p2 += 1
                d = p2 - p1
                if d > longest:
                    longest = d
            else:
                while c in collection:
                    collection.remove(s[p1])
                    p1 += 1

        return longest


if __name__ == '__main__':
    so = Solution3()
    print(so.lengthOfLongestSubstring("abcabcbb"))
    print(so.lengthOfLongestSubstring("bbbbb"))
    print(so.lengthOfLongestSubstring("pwwkew"))
    print(so.lengthOfLongestSubstring("c"))
