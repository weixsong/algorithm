"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution(object):
    """
    O(n)
    using hashset to record which char is already covered.
    """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        p1, p2 = 0, 0
        longest = p2 - p1

        coverset = set()

        while p2 < len(s):
            c2 = s[p2]
            if c2 not in coverset:
                coverset.add(c2)
                p2 += 1
                d = p2 - p1
                if d > longest:
                    longest = d
            else:
                while c2 in coverset:
                    coverset.remove(s[p1])
                    p1 += 1

        return longest
