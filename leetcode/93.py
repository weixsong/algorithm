#!/usr/bin/env python
"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""

class Solution2(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]

        Idea: DFS, add dot '.' to string s, and verify if the dot is added at valid position.
        """

        if len(s) > 12:
            return []

        res = []
        dots = []
        self.dfs(s, 0, dots, res)

        return res

    def dfs(self, s, begin, dots, res):
        # cut un-necessary dfs
        if len(s) - begin > (4 - len(dots)) * 3:
            return

        if len(dots) == 3:
            self.verify(s, dots, res)

        if begin >= len(s):
            return

        for i in range(1, 4):
            pos = begin + i
            if pos >= len(s):
                continue

            temp = s[begin:pos]
            if int(temp) > 255 or (len(temp) > 1 and temp[0] == '0'):
                continue

            dots.append(pos)
            self.dfs(s, pos, dots, res)
            dots.pop()

    def verify(self, s, dots, res):
        pre = 0
        temp = ''
        for pos in dots:
            num = s[pre:pos]
            pre = pos
            temp += num + '.'

        num = s[pre:]
        if int(num) > 255 or (len(num) > 1 and num[0] == '0'):
            return
        temp += num

        res.append(temp)

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]

        Idea: DFS, using chunking
        using chunking is more easy to understand
        """
        if len(s) > 12:
            return []

        res = []
        chunks = []
        self.dfs(s, chunks, res)
        return res

    def dfs(self, s, chunks, res):
        if len(s) > (4 - len(chunks)) * 3 or len(s) == 0:
            return

        if len(chunks) == 3:
            # candidate
            self.verify(s, chunks, res)
            return

        for i in range(1, 4):
            chunk = s[:i]
            if chunk == '' or int(chunk) > 255 or (len(chunk) > 1 and chunk[0] == '0'):
                break

            chunks.append(chunk)
            self.dfs(s[i:], chunks, res)
            chunks.pop()

    def verify(self, s, chunks, res):
        if len(s) == 0 or int(s) > 255 or (len(s) > 1 and s[0] == '0'):
            return

        chunks.append(s)
        res.append('.'.join(chunks))
        chunks.pop()
        

if __name__ == '__main__':
    so = Solution()

    res = so.restoreIpAddresses('25525511135')
    print res

    res = so.restoreIpAddresses('0000')
    print res

    res = so.restoreIpAddresses("010010")
    print res

