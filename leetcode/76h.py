# -*- encoding: utf-8 -*-
'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
'''

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        missing = len(t)
        need = {}

        for c in t:
            need[c] = need.get(c, 0) + 1

        left, right = 0, 0
        i, j = 0, 0

        for j, c in enumerate(s, 1):
            if c not in need:
                need[c] = 0

            missing -= need[c] > 0
            need[c] -= 1

            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1

                if not right or j - i <= right - left:
                    left, right = i, j

        return s[left:right]

if __name__ == '__main__':
    so = Solution()

    print so.minWindow('a', 'a')
