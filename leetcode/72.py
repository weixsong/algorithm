# -*- encoding: utf-8 -*-
'''
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
'''

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        m, n = len(word1), len(word2)
        dist = [[0 for j in range(n + 1)] for i in range(m + 1)]
        dist[0][0] = 0

        for i in range(1, m + 1):
            dist[i][0] = i

        for j in range(1, n + 1):
            dist[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dist[i][j] = dist[i - 1][j - 1]
                else:
                    dist[i][j] = min(dist[i - 1][j - 1], dist[i - 1][j], dist[i][j - 1]) + 1

        return dist[-1][-1]
