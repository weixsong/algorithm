#!/usr/bin/env python
"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int

        Idea: Dynamic programming

        f(i,j): shortest path from top to [i, j]
        f(i,j) = min(f(i - 1, j), f(i - 1, j - 1))
        need to check if left or right parent of current position is exist.

        Time: O(mn)
        Space: O(mn), could be O(n)
        """
        if triangle == None or len(triangle) == 0:
            return 0

        m = len(triangle)
        mat = triangle

        for i in range(1, m):
            for j in range(i + 1):
                left, right = float('inf'), float('inf')
                if j - 1 < i and j - 1 >= 0:
                    right = mat[i - 1][j - 1]
                if j < i and j >= 0:
                    left = mat[i - 1][j]

                mat[i][j] += min(left, right)

        return min(mat[-1])

if __name__ == '__main__':
    so = Solution()

    print so.minimumTotal([[1],[2,3]])
