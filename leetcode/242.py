# -*- encoding: utf-8 -*-
'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.
'''

class Solution2(object):
    '''
    Line 16: RuntimeError: maximum recursion depth exceeded in cmp
    '''
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack = []
        self.dfs(s, t, 0, 0, stack)
        return len(stack) == 0

    def dfs(self, s, t, i, j, stack):
        if i == len(s) and j == len(t):
            return

        if j < len(t) and len(stack) > 0 and t[j] == stack[len(stack) - 1]:
            stack.pop()
            self.dfs(s, t, i, j + 1, stack)

        elif i < len(s):
            stack.append(s[i])
            self.dfs(s, t, i + 1, j, stack)

class Solution1(object):
    '''
    wrong
    '''
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        i, j = 0, 0
        stack = []

        while i < len(s):
            if j < len(t) and len(stack) > 0 and stack[len(stack) - 1] == t[j]:
                stack.pop()
                j += 1
            else:
                stack.append(s[i])
                i += 1

        while j < len(t) and len(stack) > 0 and stack[len(stack) - 1] == t[j]:
            stack.pop()
            j += 1

        print stack
        if j != len(t):
            return False
        return len(stack) == 0

## previous idea is totally wrong

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
    
        sd, td = {}, {}
        for c in s:
            if c not in sd:
                sd[c] = 0
            sd[c] = sd[c] + 1
            
        for c in t:
            if c not in td:
                td[c] = 0
            td[c] = td[c] + 1
            
        for key in sd:
            if key not in td:
                return False
            else:
                if sd[key] != td[key]:
                    return False
                    
        return True

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        while s != '':
            if len(s) != len(t):
                return False
            tmp = s[0]
            s = s.replace(tmp, '')
            if tmp not in t:
                return False
                
            t = t.replace(tmp, '')

        if t != '':
            return False
        else:
            return True

class Solution(object):
    def isAnagram(self, s, t):
        ts = set(t)
        while s != '':
            if len(s) != len(t):
                return False
            tmp = s[0]
            s = s.replace(tmp, '')
            if tmp not in ts:
                return False
                
            t = t.replace(tmp, '')
            ts.remove(tmp)

        if t != '':
            return False
        else:
            return True
        


if __name__ == '__main__':
    so = Solution()

    print so.isAnagram('anagram', 'nagaram')
    print so.isAnagram('rat', 'car')
    print so.isAnagram('a', 'ab')
    print so.isAnagram("dgqztusjuu", "dqugjzutsu")
    print so.isAnagram("aba", "ab")