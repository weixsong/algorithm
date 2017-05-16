# -*- encoding: utf-8 -*-
'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        res = []
        comb = []
        self.dfs(1, n, k, res, comb)
        return res

    def dfs(self, begin, end, k, res, comb):
        if len(comb) == k:
            res.append(comb[:])
            return

        for i in range(begin, end + 1):
            comb.append(i)
            self.dfs(i + 1, end, k, res, comb)
            comb.pop()

if __name__ == '__main__':
    so = Solution()

    print so.combine(4, 2)
