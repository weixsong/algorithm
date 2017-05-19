#!/usr/bin/env python
"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
"""

class Solution2(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool


        Definitly time out
        Time: O(2^n)
        """
        
        if len(s1) + len(s2) != len(s3):
            return False

        l1 = list(s1 + s2)
        l3 = list(s3)

        l1.sort()
        l3.sort()

        if l1 != l3:
            return False

        self.record = {}
        return self.dp(s1, s2, s3)

    def dp(self, s1, s2, s3):
        if len(s1) == 0 and s2 == s3:
            return True
        elif len(s1) == 0 and s2 != s3:
            return False

        if len(s2) == 0 and s1 == s3:
            return True
        elif len(s2) == 0 and s1 != s3:
            return False

        if s1[0] == s2[0]:
            if s3[0] == s1[0]:
                return self.dp(s1[1:], s2, s3[1:]) or self.dp(s1, s2[1:], s3[1:])
            else:
                return False
        else:
            if s1[0] == s3[0]:
                return self.dp(s1[1:], s2, s3[1:])
            elif s2[0] == s3[0]:
                return self.dp(s1, s2[1:], s3[1:])
            else:
                return False

class Solution3(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False

        self.visited = set()
        return self.search(s1, s2, s3, 0, 0)

    def search(self, s1, s2, s3, i1, i2):
        self.visited.add((i1, i2))
        if i1 + i2 == len(s3):
            return True
        else:
            if i1 < len(s1) and s1[i1] == s3[i1 + i2] and (i1+1, i2) not in self.visited and self.search(s1, s2, s3, i1+1, i2):
                return True

            if i2 < len(s2) and s2[i2] == s3[i1 + i2] and (i1, i2+1) not in self.visited and self.search(s1, s2, s3, i1, i2+1):
                return True

        return False

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool

        Idea: dynamic programming
        f(i, j): if pointer i, j are currently interleaving for s3

        f(i, j) = f(i - 1, j) or f(i, j - 1)

        f(i, j) =       OR  | f(i - 1, j) && s1[i] == s3[p]
        p = i + j - 1       | f(i, j - 1) && s2[j] == s3[p]
        """

        if len(s1) + len(s2) != len(s3):
            return False

        m, n = len(s1), len(s2)
        mat = [[False for j in range(n + 1)] for i in range(m + 1)]
        mat[0][0] = True

        for i in range(1, m + 1):
            mat[i][0] = mat[i - 1][0] and (s1[i - 1] == s3[i - 1])

        for j in range(1, n + 1):
            mat[0][j] = mat[0][j - 1] and (s2[j - 1] == s3[j - 1])

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                p = i + j - 1
                mat[i][j] = (mat[i-1][j] and (s1[i-1] == s3[p])) or (mat[i][j-1] and (s2[j-1] == s3[p]))

        return mat[-1][-1]

if __name__ == '__main__':
    so2 = Solution2()

    print so2.isInterleave('aa', 'ab', 'abaa')
    print so2.isInterleave('aabd', 'abdc', 'aabdbadc')
    print so2.isInterleave('aabcc', 'dbbca', 'aadbbcbcac')
    print so2.isInterleave('aabcc', 'dbbca', 'aadbbbaccc')

    so = Solution()
    print '----------'
    print so.isInterleave('aa', 'ab', 'abaa')
    print so.isInterleave('aabcc', 'dbbca', 'aadbbcbcac')
    print so.isInterleave('aabcc', 'dbbca', 'aadbbbaccc')

