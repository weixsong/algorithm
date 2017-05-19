# -*- encoding: utf-8 -*-
'''
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Update (2014-11-02):
The signature of the function had been updated to return the index instead of the pointer. If you still see your function signature returns a char * or String, please click the reload button  to reset your code definition.
'''

class Solution2(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        return haystack.find(needle)

class Solution(object):
    '''
    Implement KMP algorithm by self
    O(n + m)
    '''
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        next = self.get_next(needle)
        i, j = 0, 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1

            else:
                if j > 0:
                    j = next[j - 1]
                else:
                    i += 1

        if j == len(needle):
            return i - len(needle)
        return -1

    def get_next(self, pattern):
        next = [0 for c in pattern]

        for i in range(1, len(pattern) - 1):
            k = next[i - 1]

            while pattern[i] != pattern[k] and k != 0:
                k = next[k - 1]

            if pattern[i] == pattern[k]:
                next[i] = next[k] + 1
            else:
                next[i] = 0

        return next

if __name__ == '__main__':
    so = Solution()
    print so.strStr("mississippi", "a")


