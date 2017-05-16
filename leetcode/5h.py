'''
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
'''

class Solution3:
    '''
    brute force algorithm, check all possible substring.
    O(n^3)
    this is reallys bad.
    '''
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        if s == None: return None

        max_len = 0
        longestPalindrome = None

        for i in range(len(s)):
            for j in range(i, len(s)):
                substr = s[i:j + 1]
                if self.isPalindrome(substr):
                    if len(substr) > max_len:
                        max_len = len(substr)
                        longestPalindrome = substr

        return longestPalindrome

    def isPalindrome(self, str):
        i, j = 0, len(str) - 1
        while i <= j:
            if str[i] != str[j]:
                return False
            i += 1
            j -= 1

        return True

class Solution2s:
    '''
    O(2^n)
    dynamic programming, recursive call.
    This really bad. too much recursive call, and recompute the same sub problem multiply times.
    '''
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        if s == None: return None
        if len(s) <= 1: return s

        i, j = self.find(s, 0, len(s) - 1)

        return s[i:j+1]

    def find(self, s, i, j):
        '''
        recursive call to find palindrome
        '''

        # base case
        if i == j: return i, j
        elif i + 1 == j and s[i] == s[j]: return i, j
        else:
            if s[i] == s[j]:
                r1, r2 = self.find(s, i+1, j-1)
                if r1 == i+1 and r2 == j-1: return i, j

            r1, r2 = self.find(s, i, j-1)
            r3, r4 = self.find(s, i+1, j)
            if r2 - r1 > r4 - r3: return r1, r2
            else: return r3, r4

class Solution2:
    '''
    O(n^2)
    space: O(n^2)
    dynamic programming, using back trace to compute palindrome.
    This algorithm is not good enough.
    '''
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        if s == None: return None
        if len(s) <= 1: return s

        max_len = 0
        longest = ''

        table = [[0 for j in range(len(s))] for i in range(len(s))]

        for i in range(len(s)):
            table[i][i] = 1

        for i in range(len(s) - 1):
            if s[i] == s[i+1]: table[i][i+1] = 1

        begin_len = 3
        for length in range(begin_len, len(s) + 1):
            for i in range(len(s) - length + 1):
                j = i + length - 1
                if s[i] == s[j] and table[i+1][j-1] == 1:
                    table[i][j] = 1
                    if length > max_len:
                        max_len = length
                        longest = s[i:j+1]

        return longest

class Solution1:
    '''
    find palindrom for each char in the string. some trick for odd/even palindrome
    O(n^2)
    space: O(1)
    could pass leetcode
    '''
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        if s == None: return None
        if len(s) <= 1: return s

        longest = ''
        for i in range(len(s)):
            temp = self.find(s, i, i)
            if len(temp) > len(longest): longest = temp

            temp = self.find(s, i, i + 1)
            if len(temp) > len(longest): longest = temp

        return longest

    def find(self, s, left, right):
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left+1:right]

class Solution:
    '''
    using symmetric information of already checked substring.
    O(n)
    space: O(n)
    '''
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        if s == None: return None
        if len(s) <= 1: return s

        longest, mid = 0, 0

        s2 = '#'.join(s)
        s2 = '#' + s2 + '#'

        p = [1 for i in range(len(s2))] # radius of palindrome of each char

        center, maxid = 0, 0
        for i in range(len(s2)):
            if maxid > i:
                sym = 2 * center - i # find symmetric point
                if sym >= 0: p[i] = min(p[sym], maxid - i)
                else: p[i] = maxid - i

            while i- p[i] >= 0 and i + p[i] < len(s2) and s2[i- p[i]] == s2[i + p[i]]:
                p[i] += 1

            if p[i] + i > maxid:
                maxid = p[i] + i
                center = i
            if p[i] > longest: 
                longest = p[i]
                mid = i

        # construct results string
        res = []
        for i in range(mid - longest + 1, mid + longest):
            if s2[i] != '#': res.append(s2[i])

        return ''.join(res)      


if __name__ == '__main__':
    
    #so = Solution()
    so = Solution2s()

    s1 = ''
    s2 = 'a'
    s3 = 'ab'
    s4 = '123aba'
    s5 = '123abcba23'
    s6 = '123abccba23'
    s7 = 'ccc'
    s8 = 'accc'
    s9 = 'abbbbbba'
    s10 = "aaabaaaa"
    s11 = 'tattarrattat'
    s12 = 'abaaaa'
    s13 = "bananas"

    s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"


    print so.longestPalindrome(s1)
    print so.longestPalindrome(s2)
    print so.longestPalindrome(s3)
    print so.longestPalindrome(s4)
    print so.longestPalindrome(s5)
    print so.longestPalindrome(s6)
    print so.longestPalindrome(s7)
    print so.longestPalindrome(s8)
    print so.longestPalindrome(s9)
    print so.longestPalindrome(s10)
    print so.longestPalindrome(s11)
    print so.longestPalindrome(s12)
    print so.longestPalindrome(s13)




