#!/usr/bin/env python
"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []

        res = [1]
        for i in range(rowIndex):
            next = [1]
            if len(res) >= 2:
                for j in range(len(res) - 1):
                    next.append(res[j] + res[j + 1])
            next.append(1)
            res = next

        return res
