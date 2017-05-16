# -*- encoding: utf-8 -*-
'''
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
'''

class Solution2(object):
    '''
    dynamic programming
    timeout
    '''
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        i = len(s) - 1
        j = len(p) - 1

        return self.dp(s, p, i, j)

    def dp(self, s, p, i, j):
        if i < 0 and j < 0:
            return True

        if i >= 0 and j < 0:
            return False

        if i < 0 and j >= 0 and p[j] != '*':
            return False

        if i < 0 and j > 0 and p[j] == '*':
            return self.dp(s, p, i, j - 2)

        if p[j] != '*' and p[j] != '.' and s[i] != p[j]:
            return False

        if p[j] != '*' and p[j] != '.' and s[i] == p[j]:
            return self.dp(s, p, i - 1, j - 1)

        if p[j] == '*' and j > 0:
            c = p[j - 1]
            if c == '.' or c == s[i]:
                res1 = self.dp(s, p, i - 1, j)
                res2 = self.dp(s, p, i, j - 2)
                if res1 or res2:
                    return True
                else:
                    return False
            else:
                return self.dp(s, p, i, j - 2)

        if p[j] == '*' and j == 0:
            return False

        if p[j] == '.':
            return self.dp(s, p, i - 1, j - 1)

        return False
        

class Solution(object):
    '''
    dynamic programming
    from small problem to bigger problem
    from bottom to top
    '''
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        table = [[False] * (len(s) + 1) for c in range(len(p) + 1)]

        # empty s and empty p is true
        table[0][0] = True

        # udpate corner case, p[i] == '*'
        # empty s and p
        for i in range(2, len(p) + 1):
            if p[i - 1] == '*':
                table[i][0] = table[i - 2][0]

        # update
        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != '*':
                    # Update the table by referring the diagonal element.
                    if p[i - 1] == '.' or p[i - 1] == s[j - 1]:
                        table[i][j] = table[i - 1][j - 1]

                else:
                    # eliminate previous or count previous
                    # Eliminations (referring to the vertical element)
                    # Either refer to the one before previous or the previous.
                    # I.e. * eliminate the previous or count the previous.
                    # [test_symbol_1]
                    if table[i - 2][j] == True:
                        table[i][j] = True
                    else:
                        table[i][j] = table[i - 1][j]

                    # Propagations (referring to the horizontal element)
                    # If p's previous one is equal to the current s, with
                    # helps of *, the status can be propagated from the left.
                    # [test_symbol_2]
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        table[i][j] |= table[i][j - 1]

        return table[-1][-1]

if __name__ == '__main__':
    so = Solution()

    s1 = 'aa'
    p1 = 'a'

    s2 = 'aa'
    p2 = 'aa'

    s3 = 'aaa'
    p3 = 'aa'

    s4 = 'aa'
    p4 = 'a*'

    s5 = 'ab'
    p5 = '.*'

    s6 = 'ab'
    p6 = '.*'

    s7 = 'aab'
    p7 = 'c*a*b'

    s7 = 'aab'
    p7 = 'c*a*b'

    s8 = 'aaa'
    p8 = 'a*a'

    s9 = 'aaa'
    p9 = 'ab*ac*a'

    s10 = 'aaa'
    p10 = 'ab*a*c*a'

    s11 = "aasdfasdfasdfasdfas"
    p11 = "aasdf.*asdf.*asdf.*asdf.*s"


    print so.isMatch(s1, p1)
    print so.isMatch(s2, p2)
    print so.isMatch(s3, p3)
    print so.isMatch(s4, p4)
    print so.isMatch(s5, p5)
    print so.isMatch(s6, p6)
    print so.isMatch(s7, p7)
    print so.isMatch(s8, p8)
    print so.isMatch(s9, p9)
    print so.isMatch(s10, p10)

