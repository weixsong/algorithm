# -*- encoding: utf-8 -*-
'''
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
'''

'''
f(i,j) = f(i - 1, j - 1) if p[i] == '?' or p[i] == s[j]
f(i,j) = f(i, j - 1) or f(i - 1, j) if p[i] == '*'

f(0, j) = 0
f(i, 0) = f(i - 1, j) if p[i] == '*'
        = 0 if p[i] != '*'
'''

class Solution1(object):
    '''
    Dynamic programming
    O(n^2)
    timeout
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
        for i in range(1, len(p) + 1):
            if p[i - 1] == '*':
                table[i][0] = table[i - 1][0]

        # update
        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != '*':
                    # Update the table by referring the diagonal element.
                    if p[i - 1] == '?' or p[i - 1] == s[j - 1]:
                        table[i][j] = table[i - 1][j - 1]

                else:
                    table[i][j] = table[i][j - 1] or table[i - 1][j]

        return table[-1][-1]

class Solution(object):
    '''
    Greedy Algorithm, move p pointer first always
    '''
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        sp, pp = 0, 0
        last_s = 0
        last_star = None

        while sp < len(s):
            # if match, advancing both pointers
            if pp < len(p) and (p[pp] == '?' or s[sp] == p[pp]):
                sp += 1
                pp += 1
                continue

            # * found, only advancing pattern pointer
            # let * represent empty string
            if pp < len(p) and p[pp] == '*':
                last_star = pp
                last_s = sp
                pp += 1
                continue

            # last pattern pointer was *, advancing string pointer and 
            # move back pattern pointer to next char of last *
            # let * represent a char, then advancing string pointer
            if last_star != None:
                pp = last_star + 1
                last_s += 1
                sp = last_s
                continue

            return False

        while pp < len(p) and p[pp] == '*':
            pp += 1

        return pp == len(p)


if __name__ == '__main__':
    so = Solution()

    print so.isMatch("aa","a")
    print so.isMatch("aa","aa")
    print so.isMatch("aaa","aa")
    print so.isMatch("aa", "*")
    print so.isMatch("aa", "a*")
    print so.isMatch("ab", "?*")
    print so.isMatch('aab', 'c*a*b')

