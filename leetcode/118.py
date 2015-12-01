#!/usr/bin/env python
"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        res = []
        if numRows < 1:
            return res

        res.append([1])

        for i in range(numRows - 1):
            last = res[-1]
            added = [1]
            if len(last) >= 2:
                for j in range(len(last) - 1):
                    added.append(last[j] + last[j + 1])
            added.append(1)
            res.append(added)

        return res

if __name__ == '__main__':
    so = Solution()

    res = so.generate(5)

    for row in res:
        print row