#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
'''

class Solution(object):
    '''
    worst case: O(2^n)
    total 2^n different cases for partition
    '''
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        res = []
        comb = []
        self.dfs(s, 0, res, comb)

        return res

    def dfs(self, s, idx, res, comb):
        if idx == len(s):
            res.append(comb[:])
            return

        for i in range(idx, len(s)):
            if self.is_palindrom(s, idx, i) == False:
                continue

            part = s[idx: i + 1]
            comb.append(part)
            self.dfs(s, i + 1, res, comb)
            comb.pop()

    def is_palindrom(self, s, left, right):
        while left <= right and left >= 0 and right <= len(s) - 1:
            if s[left] != s[right]: return False
            left += 1
            right -= 1

        return True

if __name__ == '__main__':
    so = Solution()
    res = so.partition('aab')
    print res

    print so.partition('efe')
