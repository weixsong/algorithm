# -*- encoding: utf-8 -*-
'''
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.
'''

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = s.strip()
        n = len(s)

        if n == 0:
            return False

        i = 0
        if s[i] == '+' or s[i] == '-':
            i += 1

        num_count, point_count = 0, 0
        while i < n and (s[i].isdigit() or s[i] == '.'):
            if s[i] == '.':
                point_count += 1
            else:
                num_count += 1

            i += 1

        if num_count < 1 or point_count > 1:
            return False

        if i == n:
            return True

        if s[i] == 'e':
            i += 1
            if i == n:
                return False

            num_count, point_count = 0, 0
            if s[i] == '+' or s[i] == '-':
                i += 1
            while i < n and (s[i].isdigit() or s[i] == '.'):
                if s[i] == '.':
                    point_count += 1
                else:
                    num_count += 1

                i += 1

            if num_count < 1 or point_count > 0:
                return False

        return i == n

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        import re
        s = s.strip()

        if re.match('^[+-]?(([0-9]*\.?[0-9]+)|([0-9]+\.?[0-9]*))([Ee][+-]?[0-9]+)?$', s):
            return True
        else:
            return False

